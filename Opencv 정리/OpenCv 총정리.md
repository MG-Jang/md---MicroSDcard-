# OpenCv 정리

영상처리에 특화된 오픈소스라이브러리

예시 코드 로 설명
```c++
#include <opencv2/opencv.hpp>

using namespace cv; // cv::내용~ 앞에 cv적는 것을 빼기위해 사용 
using namespace std;

int main(int ac, char** av) {

	VideoCapture cap("test.mp4");
	//cap.set(CV_CAP_PROP_FRAME_WIDTH, 1920);
	//cap.set(CV_CAP_PROP_FRAME_HEIGHT, 1080);

	if (!cap.isOpened())
	{
		printf("Can't open the camera");
		return -1;
	}

	Mat img; // Mat(대문자 주의) 은 행렬(matrix) 의 약자로 주로 이미지 히스토그램 등을 저장
	while (1)
	{
		cap >> img; // cap영상을 프레임 단위로 img 로 변화.
        cvtColor(img, hsv, COLOR_RGB2HSV);// (원본이미지,변환이미지,변환형식)

		if (img.empty())  // 영상에서 더이상 보낼 이미지가 없으면 프로그램 종료
		{
			printf("empty image");
			return 0;
		}
        
		imshow("camera img", img);
        imshow("camera hsv", hsv);

		if (waitKey(25) == 27) //이게 없으면 영상이 연속적으로 안나옴. 나도 왜 그런지 모르겠다.
			break;
	}


	return 0;
}

```