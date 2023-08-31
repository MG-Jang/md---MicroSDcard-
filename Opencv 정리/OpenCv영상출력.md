# OpenCV 영상출력

아래 예제코드 실행시 test.mp4를 실행하기 위해서는<br>
test.mp4파일을 솔루션 탐색기 -> 리소스 파일 안에 넣어야 한다.<br>
if 만약 실행이 안되면 해당main.cpp파일이 있는 폴더에 영상을 넣어 보자. 


예제 코드
```C++
#include <opencv2/opencv.hpp>

using namespace cv;
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

	Mat img;

	while (1)
	{
		cap >> img;
        
		if (img.empty())
		{
			printf("empty image");
			return 0;
		}
        
		imshow("camera img", img);

		if (waitKey(25) == 27)
			break;
	}


	return 0;
}
```