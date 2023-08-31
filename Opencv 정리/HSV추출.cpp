//RGB사진을 HSV로 변환 후 HSV에서 H, S, V 각각의 속성을 추출

#include <iostream>
#include <opencv2/opencv.hpp>
 
using namespace std;
using namespace cv;
 
int main() {
    Mat image = imread("boldt.jpg"); //read a image
    Mat hsv;
    cvtColor(image, hsv, COLOR_BGR2HSV); //convert BGR to HSV
    vector<Mat>  channels;
    split(hsv, channels); //split to h,s,v
    //channels[0] 색상(H),  channels[1]  채도(S),  channels[2]  명도(V)
    //각 채널 출력
    imshow("Original", image); //original
    imshow("Hue", channels[0]); //hue
    imshow("Saturate", channels[1]); //saturate
    imshow("Value", channels[2]); //value
    //channels[2] = 255; //value to max  value 값을 바꾸면 어떻게 될까 추측
    merge(channels, hsv); //merge h,s,v  hsv요소들 결합. 
    Mat newImage;
    cvtColor(hsv, newImage, COLOR_HSV2BGR); //convert HSV to BGR
    imshow("Fixed Value Image", newImage);
    waitKey(0);
 
    return 0;
}