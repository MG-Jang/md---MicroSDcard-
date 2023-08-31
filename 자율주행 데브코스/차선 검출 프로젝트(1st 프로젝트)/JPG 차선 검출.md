JPG를 이용하여 차선 검출
실행시 차선이 검출되어야함

```c
#include <iostream>
#include "opencv2/opencv.hpp"

using namespace std;
using namespace cv;
// p1,p2 왼쪽 차선
const Point p1(300, 600), p2(500, 600);
// p3,p4 오른쪽 차선
const Point p3(800, 600), p4(1000, 600);

vector<Point2f> find_edges(const Mat& img);
void drawCross(Mat& img, Point pt, Scalar color);

int main()
{
    Mat src = imread("lane02.JPG", IMREAD_COLOR); // lane 영상 불러오기 (COLOR)

    if (src.empty()) {
        cerr << "Image laod failed!" << endl;
        return -1;
    }

    Mat gray;
    cvtColor(src, gray, COLOR_BGR2GRAY); // COLOR로 불러온 영상 GRAYSCALE로 변환

    // 왼쪽 차선 및 오른쪽 차선 검출을 위한 사각형 영역
    Rect rc1(p1 + Point(0, -10), p2 + Point(0, 10));
    Rect rc2(p3 + Point(0, -10), p4 + Point(0, 10));
    // 주어진 ROI에서 find_edges 함수를 이용하여 Edge 검출
    vector<Point2f> pts1 = find_edges(gray(rc1));
    vector<Point2f> pts2 = find_edges(gray(rc2));

    Mat dst = src.clone(); //LINE을 그리기 위해서 COLOR 영상으로 변환
    line(dst, p1, p4, Scalar(0, 255, 128), 1, LINE_AA); //Line 그리기

    // 왼쪽 차선 위치 표시
    drawCross(dst, Point(cvRound(p1.x + pts1[0].x), p1.y), Scalar(255, 0, 0));
    drawCross(dst, Point(cvRound(p1.x + pts1[1].x), p1.y), Scalar(0, 0, 255));
    putText(dst, format("(%4.3f, %d)", p1.x + pts1[0].x, p1.y),
        Point(p1.x + pts1[0].x - 50, p1.y - 20),
        FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 0, 0), 1, LINE_AA);
    putText(dst, format("(%4.3f, %d)", p1.x + pts1[1].x, p1.y),
        Point(p1.x + pts1[1].x - 20, p1.y + 30),
        FONT_HERSHEY_SIMPLEX, 0.5, Scalar(0, 0, 255), 1, LINE_AA);

    // 오른쪽 차선 표시
    drawCross(dst, Point(cvRound(p3.x + pts2[0].x), p3.y), Scalar(255, 0, 0));
    drawCross(dst, Point(cvRound(p3.x + pts2[1].x), p3.y), Scalar(0, 0, 255));
    putText(dst, format("(%4.3f, %d)", p3.x + pts2[0].x, p3.y),
        Point(p3.x + pts1[0].x - 50, p3.y - 20),
        FONT_HERSHEY_SIMPLEX, 0.5, Scalar(255, 0, 0), 1, LINE_AA);
    putText(dst, format("(%4.3f, %d)", p3.x + pts2[1].x, p3.y),
        Point(p3.x + pts1[1].x - 20, p3.y + 30),
        FONT_HERSHEY_SIMPLEX, 0.5, Scalar(0, 0, 255), 1, LINE_AA);

    imshow("dst", dst);
    waitKey();
}

// img 영상의 세로 좌표 중간에서 가로 방향 에지의 시작과 끝 좌표를 계산하여 반환
vector<Point2f> find_edges(const Mat& img)
{
    // 가우시안, 1차 미분 등의 연산은 실수형으로 수행함
    Mat fimg, blr, dx;
    img.convertTo(fimg, CV_32F); // 정수형으로 정의된  img 를 실수형으로 변환 fimg
    GaussianBlur(fimg, blr, Size(), 1.); // 가우시안 블러 , 노이즈 제거
    Sobel(blr, dx, CV_32F, 1, 0);  // Sobel 필터
    imshow("img", img);
    imshow("dx", dx);

    double minv, maxv;
    Point minloc, minloc1, minloc2, maxloc, maxloc1, maxloc2;

    int y2 = img.rows / 2;
    Mat roi = dx.row(y2); // Y

    minMaxLoc(roi, &minv, &maxv, &minloc, &maxloc); // Y

#if 0
    vector<Point2f> pts;
    pts.push_back(Point2f(maxloc.x, y2));
    pts.push_back(Point2f(minloc.x, y2));


#else
    vector<Point2f> pts;
    // 서브픽셀 정확도로 에지 위치를 찾아 pts에 저장하는 코드를 작성하세요!
    float X = roi.at<float>(maxloc.x - 1); // X -1의 위치
    float Y = roi.at<float>(maxloc.x); // Y 0의 위치
    float Z = roi.at<float>(maxloc.x + 1); // Z 1의 위치
    pts.push_back(Point2f(maxloc.x + (X - Z) / (2 * X - 4 * Y + 2 * Z), y2)); // 평행이동 +maxloc.x

    X = roi.at<float>(minloc.x - 1); // X -1의 위치
    Y = roi.at<float>(minloc.x); // Y 0의 위치
    Z = roi.at<float>(minloc.x + 1); // Z 1의 위치
    pts.push_back(Point2f(minloc.x + (X - Z) / (2 * X - 4 * Y + 2 * Z), y2)); // 평행이동 +maxloc.x

#endif

    return pts;
}
// x 표시로 라인을 그려주는 함수
void drawCross(Mat& img, Point pt, Scalar color)
{
    int span = 5; // X 표시의 길이
    line(img, pt + Point(-span, -span), pt + Point(span, span), color, 1, LINE_AA);
    line(img, pt + Point(-span, span), pt + Point(span, -span), color, 1, LINE_AA);
}
```