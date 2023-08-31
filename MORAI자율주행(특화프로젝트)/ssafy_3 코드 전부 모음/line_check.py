import cv2
#import youtube_dl
#import pafy
import numpy as np
import matplotlib.pyplot as plt
import time

import os, rospkg
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridgeError

#url = 'https://www.youtube.com/watch?v=ipyzW38sHg0'
#video = pafy.new(url)
#best = video.getbest(preftype = 'mp4')

#cap = cv2.VideoCapture(best.url)

ym_per_pix = 30 / 720
xm_per_pix = 3.7 / 720


frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out1 = cv2.VideoWriter('C:\\Users\\bit\\Desktop\\opencv_youtube.mp4', fourcc, 20.0, frame_size)


class IMGParser:
    def __init__(self):

        self.image_sub = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.callback)

    def callback(self, msg):
        try:
            #TODO: (1)
            '''
            # Open CV 를 이용하여 Camera 데이터를 시각화 하기 위해서는 np.array 형태가 필요하다. 
            # Byte 단위로 저장 된 이미지 데이터를 np.array 형태로 읽는 부분이다.
            # np.fromstring 함수를 이용하여 읽어오는 data 정보를 uint8 형태로 변환한다.

            np_arr = np.fromstring(         )

            '''
            np_arr = np.fromstring(msg.data, np.uint8)

            #TODO: (2)
            '''
            # 1차원 배열 형태로 되어있는 np_arr 변수를 3차원 배열로 만든뒤 컬러 이미지로 변환합니다.
            # cv2.imdecode 함수를 이용하여 np_arr 변수를 3차원 배열로 만듭니다.
            # cv2.IMREAD_COLOR 함수를 통해 이미지 파일을 bgr 형태의 Color로 읽어들입니다.

            img_bgr = cv2.imdecode(         )

            '''
            img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            cap = cv2.VideoCapture(img_bgr)
        except CvBridgeError as e:
            print(e)

        #TODO: (3)
        '''
        # 이미지를 출력 합니다.
        # cv2.imshow 함수를 이용하여 이미지를 실시간으로 출력합니다.
        # cv2.waitKey 함수를 이용하여 이미지 업데이트 시간을 지연 시킬 수 있습니다.
        # cv2.waitKey 함수의 단위는 ms 입니다.

        cv2.imshow(             )
        cv2.waitKey(            ) 

        '''

        cv2.imshow('Image window2', img_bgr)   # 'Image window2'는 띄우는 창의 이름이므로 크게 중요하지 않다.
        cv2.waitKey(1) 

rospy.init_node('image_parser', anonymous=True)
image_parser = IMGParser()

cap = cv2.VideoCapture(img_bgr)
ym_per_pix = 30 / 720
xm_per_pix = 3.7 / 720


frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))


def color_filter(image):
    hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    lower = np.array([20, 150, 20])
    upper = np.array([255, 255, 255])

    yellow_lower = np.array([0, 85, 81])
    yellow_upper = np.array([190, 255, 255])

    yellow_mask = cv2.inRange(hls, yellow_lower, yellow_upper)
    white_mask = cv2.inRange(hls, lower, upper)
    mask = cv2.bitwise_or(yellow_mask, white_mask)
    masked = cv2.bitwise_and(image, image, mask = mask)

    return masked

def roi(image):
    x = int(image.shape[1])
    y = int(image.shape[0])

    # 한 붓 그리기
    _shape = np.array(
        [[int(0.1*x), int(y)], [int(0.1*x), int(0.1*y)], [int(0.4*x), int(0.1*y)], [int(0.4*x), int(y)], [int(0.7*x), int(y)], [int(0.7*x), int(0.1*y)],[int(0.9*x), int(0.1*y)], [int(0.9*x), int(y)], [int(0.2*x), int(y)]])

    mask = np.zeros_like(image)

    if len(image.shape) > 2:
        channel_count = image.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    cv2.fillPoly(mask, np.int32([_shape]), ignore_mask_color)
    masked_image = cv2.bitwise_and(image, mask)

    return masked_image

def wrapping(image):
    (h, w) = (image.shape[0], image.shape[1])

    source = np.float32([[w // 2 - 30, h * 0.53], [w // 2 + 60, h * 0.53], [w * 0.3, h], [w, h]])
    destination = np.float32([[0, 0], [w-350, 0], [400, h], [w-150, h]])

    transform_matrix = cv2.getPerspectiveTransform(source, destination)
    minv = cv2.getPerspectiveTransform(destination, source)
    _image = cv2.warpPerspective(image, transform_matrix, (w, h))

    return _image, minv

def plothistogram(image):
    histogram = np.sum(image[image.shape[0]//2:, :], axis=0)
    midpoint = np.int(histogram.shape[0]/2)
    leftbase = np.argmax(histogram[:midpoint])
    rightbase = np.argmax(histogram[midpoint:]) + midpoint

    return leftbase, rightbase

def slide_window_search(binary_warped, left_current, right_current):
    out_img = np.dstack((binary_warped, binary_warped, binary_warped))

    nwindows = 4
    window_height = np.int(binary_warped.shape[0] / nwindows)
    nonzero = binary_warped.nonzero()  # 선이 있는 부분의 인덱스만 저장
    nonzero_y = np.array(nonzero[0])  # 선이 있는 부분 y의 인덱스 값
    nonzero_x = np.array(nonzero[1])  # 선이 있는 부분 x의 인덱스 값
    margin = 100
    minpix = 50
    left_lane = []
    right_lane = []
    color = [0, 255, 0]
    thickness = 2

    for w in range(nwindows):
        win_y_low = binary_warped.shape[0] - (w + 1) * window_height  # window 윗부분
        win_y_high = binary_warped.shape[0] - w * window_height  # window 아랫 부분
        win_xleft_low = left_current - margin  # 왼쪽 window 왼쪽 위
        win_xleft_high = left_current + margin  # 왼쪽 window 오른쪽 아래
        win_xright_low = right_current - margin  # 오른쪽 window 왼쪽 위
        win_xright_high = right_current + margin  # 오른쪽 window 오른쪽 아래

        cv2.rectangle(out_img, (win_xleft_low, win_y_low), (win_xleft_high, win_y_high), color, thickness)
        cv2.rectangle(out_img, (win_xright_low, win_y_low), (win_xright_high, win_y_high), color, thickness)
        good_left = ((nonzero_y >= win_y_low) & (nonzero_y < win_y_high) & (nonzero_x >= win_xleft_low) & (nonzero_x < win_xleft_high)).nonzero()[0]
        good_right = ((nonzero_y >= win_y_low) & (nonzero_y < win_y_high) & (nonzero_x >= win_xright_low) & (nonzero_x < win_xright_high)).nonzero()[0]
        left_lane.append(good_left)
        right_lane.append(good_right)
        # cv2.imshow("oo", out_img)

        if len(good_left) > minpix:
            left_current = np.int(np.mean(nonzero_x[good_left]))
        if len(good_right) > minpix:
            right_current = np.int(np.mean(nonzero_x[good_right]))

    left_lane = np.concatenate(left_lane)  # np.concatenate() -> array를 1차원으로 합침
    right_lane = np.concatenate(right_lane)

    leftx = nonzero_x[left_lane]
    lefty = nonzero_y[left_lane]
    rightx = nonzero_x[right_lane]
    righty = nonzero_y[right_lane]

    left_fit = np.polyfit(lefty, leftx, 2)
    right_fit = np.polyfit(righty, rightx, 2)

    ploty = np.linspace(0, binary_warped.shape[0] - 1, binary_warped.shape[0])
    left_fitx = left_fit[0] * ploty ** 2 + left_fit[1] * ploty + left_fit[2]
    right_fitx = right_fit[0] * ploty ** 2 + right_fit[1] * ploty + right_fit[2]

    ltx = np.trunc(left_fitx)  # np.trunc() -> 소수점 부분을 버림
    rtx = np.trunc(right_fitx)

    out_img[nonzero_y[left_lane], nonzero_x[left_lane]] = [255, 0, 0]
    out_img[nonzero_y[right_lane], nonzero_x[right_lane]] = [0, 0, 255]

    # plt.imshow(out_img)
    # plt.plot(left_fitx, ploty, color = 'yellow')
    # plt.plot(right_fitx, ploty, color = 'yellow')
    # plt.xlim(0, 1280)
    # plt.ylim(720, 0)
    # plt.show()

    ret = {'left_fitx' : ltx, 'right_fitx': rtx, 'ploty': ploty}

    return ret

def draw_lane_lines(original_image, warped_image, Minv, draw_info):
    left_fitx = draw_info['left_fitx']
    right_fitx = draw_info['right_fitx']
    ploty = draw_info['ploty']

    warp_zero = np.zeros_like(warped_image).astype(np.uint8)
    color_warp = np.dstack((warp_zero, warp_zero, warp_zero))

    pts_left = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
    pts_right = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])
    pts = np.hstack((pts_left, pts_right))

    mean_x = np.mean((left_fitx, right_fitx), axis=0)
    pts_mean = np.array([np.flipud(np.transpose(np.vstack([mean_x, ploty])))])

    cv2.fillPoly(color_warp, np.int_([pts]), (216, 168, 74))
    cv2.fillPoly(color_warp, np.int_([pts_mean]), (216, 168, 74))

    newwarp = cv2.warpPerspective(color_warp, Minv, (original_image.shape[1], original_image.shape[0]))
    result = cv2.addWeighted(original_image, 1, newwarp, 0.4, 0)

    return pts_mean, result
while True:
    retval, img = cap.read()
    if not retval:
        break

    ## 조감도 wrapped img
    wrapped_img, minverse = wrapping(img)
    # cv2.imshow('wrapped', wrapped_img)

    ## 조감도 필터링
    w_f_img = color_filter(wrapped_img)
    # cv2.imshow('w_f_img', w_f_img)

    ##조감도 필터링 자르기
    w_f_r_img = roi(w_f_img)
    # cv2.imshow('w_f_r_img', w_f_r_img)

    ## 조감도 선 따기 wrapped img threshold
    _gray = cv2.cvtColor(w_f_r_img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(_gray, 160, 255, cv2.THRESH_BINARY)
    # cv2.imshow('threshold', thresh)

    ## 선 분포도 조사 histogram
    leftbase, rightbase = plothistogram(thresh)
    # plt.plot(hist)
    # plt.show()

    ## histogram 기반 window roi 영역
    draw_info = slide_window_search(thresh, leftbase, rightbase)
    # plt.plot(left_fit)
    # plt.show()

    ## 원본 이미지에 라인 넣기
    meanPts, result = draw_lane_lines(img, thresh, minverse, draw_info)
    # cv2.imshow("result", result)

    ## 동영상 녹화
    #out1.write(result)

    key = cv2.waitKey(25)
    if key == 27:
        break


if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()