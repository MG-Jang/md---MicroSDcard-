#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>

//left파일은 img파일에 있다.

using namespace cv;

int main()
{
    // 이미지 읽기
    Mat src1 = imread("left01.jpg", IMREAD_COLOR);
    Mat src2 = imread("left02.jpg", IMREAD_COLOR);

    if (src1.empty() || src2.empty())
    {
        //std::cout << src1.empty() << std::endl;
        //std::cout << src2.empty() << std::endl;

        std::cerr << "Image load failed!" << std::endl;
    }
    // feature 객체 생성
    Ptr<Feature2D> feature = KAZE::create();
    // keypoints 벡터
    std::vector<KeyPoint> keypoints1, keypoints2;
    // descriptor 행렬
    Mat desc1, desc2;

    feature->detectAndCompute(src1, Mat(), keypoints1, desc1);
    feature->detectAndCompute(src2, Mat(), keypoints2, desc2);

    // 특징점 매칭
    Ptr<DescriptorMatcher> matcher = BFMatcher::create();
    std::vector<DMatch> matches;

    matcher->match(desc1, desc2, matches);

    // Good 매칭 선택(둘 간의 거리가 작다면 OK)
    std::sort(matches.begin(), matches.end());
    std::vector<DMatch> good_matches(matches.begin(), matches.begin() + 50);

    std::cout << "number of keypoints1 : " << keypoints1.size() << std::endl;
    std::cout << "number of keypoints2 : " << keypoints2.size() << std::endl;
    std::cout << "number of good matches : " << good_matches.size() << std::endl;

    // 매칭 결과를 dst에 그린다  
    // dst는 destination의 약자로 많이 사용된다.
    Mat dst;
    drawMatches(src1, keypoints1, src2, keypoints2, good_matches, dst,
        Scalar::all(-1), Scalar::all(-1), std::vector< char >());

    // 호모그래피를 구하기 위해 쿼리 특징점, 받는 특징점을 pts1, pts2에 옮긴다.
    std::vector<Point2f> pts1, pts2;
    for (size_t i = 0; i < good_matches.size(); i++)
    {
        pts1.push_back(keypoints1[good_matches[i].queryIdx].pt);
        pts2.push_back(keypoints2[good_matches[i].trainIdx].pt);
    }

    // 호모그래피 변환 행렬
    Mat H = findHomography(pts1, pts2, RANSAC);

    std::vector<Point2f> corners1, corners2;
    corners1.emplace_back(Point2f(0, 0));
    corners1.emplace_back(Point2f(src1.cols - 1.f, 0));
    corners1.emplace_back(Point2f(src1.cols - 1.f, src1.rows - 1.f));
    corners1.emplace_back(Point2f(0, src1.rows - 1.f));
    perspectiveTransform(corners1, corners2, H);

    // 호모그래피로 변환된 코너를 오른쪽 그림에 옮긴다.
    std::vector<Point> corners_dst;
    for (Point2f pt : corners2) {
        corners_dst.emplace_back(Point(cvRound(pt.x + src1.cols), cvRound(pt.y)));
    }
    // 호모그래피로 변환된 부분에 사각형을 그린다.
    polylines(dst, corners_dst, true, Scalar(0, 255, 0), 2, LINE_AA);
    // imshow 
    imshow("src1", src1);
    imshow("src2", src2);
    imshow("dst1", dst);
    //std::cout << "finish" << std::endl;

    waitKey();
    std::cout << "finish" << std::endl;
    std::cout << "finish" << std::endl;
    std::cout << "finish" << std::endl;
    destroyAllWindows();
    return 0;

}