# OpenCv 주요 함수 정리


|사용 용도|함수|
|---|---|
|영상 변수 선언|Mat img|
|영상출력|imshow("img_show",img)|
|이미지 복사|img.copyTo(img_copy)|
|이미지 크기 조정|resize(img, img, Size(300, 300))|
|이미지 Roi 추출|img(Rect(Point(320, 100), Point(440, 280)));|
|BGR, HSV 변환|cvtColor(img, img_hsv, COLOR_BGR2HSV)|
|RGB, GRAY 변환|cvtColor(img, img_hsv, COLOR_RGB2GRAY)|
|이진화 추출|threshold(img_houghC, img_houghC, 190, 255, THRESH_BINARY);|

