#include <iostream>
#include <vector>
#include "opencv2/opencv.hpp"

#define VIDEO_WINDOW_NAME "Video"

cv::Mat videoFrame;
cv::Mat roi;
cv::Mat dst;
cv::Mat filteredFrame;
cv::Mat edgeFrame;

std::vector<cv::Vec2f> lines1;
std::vector<cv::Vec4i> lines2;

float constrast_alpha = 1.f;


cv::Mat calcGrayHist(const cv::Mat& img)
{
	CV_Assert(img.type() == CV_8UC1);

	cv::Mat hist;
	int channels[] = { 0 };
	int dims = 1;
	const int histSize[] = { 256 };
	float graylevel[] = { 0, 256 };
	const float* ranges[] = { graylevel };

	calcHist(&img, 1, channels, cv::noArray(), hist, dims, histSize, ranges);

	return hist;
}

void calcHistStretching(const cv::Mat& img, cv::Mat& output)
{
	CV_Assert(img.type() == CV_8UC1);

	double gmin, gmax;
	cv::minMaxLoc(img, &gmin, &gmax);

	output = (img - gmin) * 255 / (gmax - gmin);
}

void calcHistEqualization(const cv::Mat& img, cv::Mat& output)
{
	CV_Assert(img.type() == CV_8UC1);

	cv::equalizeHist(img, output);
}

void sharpenGaussian(const cv::Mat& img, cv::Mat& output, float alpha)
{
	cv::GaussianBlur(img, output, cv::Size(), 1);

	output = (1.f + alpha) * img - alpha * output;
}


void sobleEdge(const cv::Mat& img, cv::Mat& output, cv::Mat& sobel_dx, cv::Mat& sobel_dy)
{
	cv::Sobel(img, sobel_dx, CV_32FC1, 1, 0);
	cv::Sobel(img, sobel_dy, CV_32FC1, 0, 1);

	cv::magnitude(sobel_dx, sobel_dy, output);
	output.convertTo(output, CV_8UC1);
}

template <typename T>
void drawDetectedLines(cv::Mat& img, const std::vector<T>& lines, cv::Scalar color = cv::Scalar(255, 255, 255))
{
	for (T line : lines)
	{
		cv::line(img, cv::Point(line[0], line[1]), cv::Point(line[2], line[3]), color, 2, cv::LINE_AA);
	}
}

std::vector<cv::Point2f> findEdges(const cv::Mat& img)
{
	cv::Mat dx, dy;
	cv::Mat dstEdge;

	// 영상 명암비 조절 (Contrast)
	// dst(x,y) = saturate( src(x,y) + ( src(x,y) - 128 ) * alpha )
	dstEdge = (img + (img - 128) * constrast_alpha); // 0~256 에서 Intensity가 128 이상이면 더 밝게, 이하면 더 어둡게 설정

	// 히스토그램
	calcHistStretching(dstEdge, dstEdge);
	// 히스토그램 평활화
	cv::equalizeHist(dstEdge, dstEdge);

	dstEdge.convertTo(dstEdge, CV_32F);

	// 가우시안 블러
	//cv::GaussianBlur(dstEdge, dstEdge, cv::Size(), 1.);
	sharpenGaussian(dstEdge, dstEdge, 1.0);

	// 노이즈 제거 (양방향 필터)
	cv::bilateralFilter(dstEdge, filteredFrame, -1, 10, 5);

	// Edge 검출 (Sobel 필터)
	sobleEdge(dstEdge, edgeFrame, dx, dy); // (Sobel 필터)
	//cv::Sobel(filteredFrame, dx, CV_32F, 1, 0); // (Sobel 필터)
	//cv::Canny(filteredFrame, edgeFrame, 150, 200); // (Canny 필터)

	double minv, maxv;
	cv::Point minloc, maxloc;

	int y2 = img.rows / 2;
	cv::Mat roi = dx.row(y2);
	cv::minMaxLoc(roi, &minv, &maxv, &minloc, &maxloc);

#if 1
	std::vector<cv::Point2f> pts;
	pts.push_back(cv::Point2f(maxloc.x, y2));
	pts.push_back(cv::Point2f(minloc.x, y2));
#else
	std::vector<cv::Point2f> pts;
	// X = roi[maxloc.x -1], Y = roi[maxloc.x], Z = roi[maxloc.x + 1]
	// y = ax^2 + bx + c
	// x = -b/(2a) = (X-Z) / (2X - 4Y + 2Z)
	pts.push_back(cv::Point2f((roi[maxloc.x - 1] - roi[maxloc.x + 1]) / (2 * roi[maxloc.x - 1] - 4 * roi[maxloc.x] + 2 * roi[maxloc.x + 1]), y2));
	pts.push_back(cv::Point2f((roi[minloc.x - 1] - roi[minloc.x + 1]) / (2 * roi[minloc.x - 1] - 4 * roi[minloc.x] + 2 * roi[minloc.x + 1]), y2));
#endif

	return pts;
}

void drawCross(cv::Mat& img, cv::Point pt, cv::Scalar color)
{
	int span = 5;
	line(img, pt + cv::Point(-span, -span), pt + cv::Point(span, span), color, 1, cv::LINE_AA);
	line(img, pt + cv::Point(-span, span), pt + cv::Point(span, -span), color, 1, cv::LINE_AA);
}

int main()
{
	// 영상 가져오기
	cv::VideoCapture videoCapture("Sub_project.avi");

	if (!videoCapture.isOpened())
	{
		std::cerr << "Video load failed!" << std::endl;
	}

	// Video Info
	float videoFPS = videoCapture.get(cv::CAP_PROP_FPS);
	int videoWidth = videoCapture.get(cv::CAP_PROP_FRAME_WIDTH);
	int videoHeight = videoCapture.get(cv::CAP_PROP_FRAME_HEIGHT);

	// bounding box  point
	const cv::Point p1(0, 400), p2(int(videoWidth / 2) - 120, 400);
	const cv::Point p3(int(videoWidth / 2) + 120, 400), p4(videoWidth, 400);
	cv::Rect rc1(p1 + cv::Point(0, -10), p2 + cv::Point(0, 10));
	cv::Rect rc2(p3 + cv::Point(0, -10), p4 + cv::Point(0, 10));

	cv::namedWindow(VIDEO_WINDOW_NAME);

	while (true)
	{
		videoCapture >> videoFrame; // Get Frame from VideoCapture == videoCapture.read(videoFrame);

		if (videoFrame.empty())
		{
			std::cout << "Video END" << std::endl;
		}

		// 흑백 전환 (Grayscale)
		cv::cvtColor(videoFrame, dst, cv::COLOR_BGR2GRAY);

		// 왼쪽, 오른쪽 차선 검출 사각 영역
		std::vector<cv::Point2f> pts1 = findEdges(dst(rc1));
		std::vector<cv::Point2f> pts2 = findEdges(dst(rc2));

		cv::line(dst, p1, p4, cv::Scalar(0, 255, 128), 1, cv::LINE_AA);

		// 왼쪽 차선 위치 표시
		drawCross(dst, cv::Point(cvRound(p1.x + pts1[0].x), p1.y), cv::Scalar(255, 0, 0));
		drawCross(dst, cv::Point(cvRound(p1.x + pts1[1].x), p1.y), cv::Scalar(0, 0, 255));
		putText(dst, cv::format("(%4.3f, %d)", p1.x + pts1[0].x, p1.y),
			cv::Point(p1.x + pts1[0].x - 50, p1.y - 20),
			cv::FONT_HERSHEY_SIMPLEX, 0.5, cv::Scalar(255, 0, 0), 1, cv::LINE_AA);
		putText(dst, cv::format("(%4.3f, %d)", p1.x + pts1[1].x, p1.y),
			cv::Point(p1.x + pts1[1].x - 20, p1.y + 30),
			cv::FONT_HERSHEY_SIMPLEX, 0.5, cv::Scalar(0, 0, 255), 1, cv::LINE_AA);

		// 오른쪽 차선 위치 표시
		drawCross(dst, cv::Point(cvRound(p3.x + pts2[0].x), p3.y), cv::Scalar(255, 0, 0));
		drawCross(dst, cv::Point(cvRound(p3.x + pts2[1].x), p3.y), cv::Scalar(0, 0, 255));
		putText(dst, cv::format("(%4.3f, %d)", p3.x + pts2[0].x, p3.y),
			cv::Point(p3.x + pts1[0].x - 50, p3.y - 20),
			cv::FONT_HERSHEY_SIMPLEX, 0.5, cv::Scalar(255, 0, 0), 1, cv::LINE_AA);
		putText(dst, cv::format("(%4.3f, %d)", p3.x + pts2[1].x, p3.y),
			cv::Point(p3.x + pts1[1].x - 20, p3.y + 30),
			cv::FONT_HERSHEY_SIMPLEX, 0.5, cv::Scalar(0, 0, 255), 1, cv::LINE_AA);


		// 직선 검출 (Hough 변환)
		//cv::HoughLines(edgeFrame, lines1, 1, CV_PI / 180, 250);
		cv::HoughLinesP(edgeFrame, lines2, 1, CV_PI / 180, 160, 0, 5);


		// 이미지에 직선 그리기
		drawDetectedLines(videoFrame, lines2);


		cv::imshow(VIDEO_WINDOW_NAME, dst);

		// Exit by Press ESC
		// wait 1 / FPS (ms) for next frame  
		if (cv::waitKey(1000 / videoFPS) == 27) // cv::waitKey(num), 1000 / FPS = 초당 FPS 시간 만큼을 기다린다는 의미, '== 27'은 ESC
		{
			std::cout << "Stop Video" << std::endl;
			break;
		}
	}

	cv::destroyWindow(VIDEO_WINDOW_NAME);
	// cv::destroyALLWIndows(VIDEO_WINDOW_NAME);


	return -1;
}