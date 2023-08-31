#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from morai_msgs.msg import RadarDetections

import numpy as np

#TODO: (1) Callback 함수 생성 및 데이터 출력
def radar_callback(data):
   #  print(data)
   for det in data.detections:
      if det.azimuth != 0.0 : 
         dist = np.sqrt(det.position.x**2+det.position.y**2)
         # if(det.detection_id == 1):
         #    #print(det)
         #    print(det.position.x)
         if dist < 10 :
            #print(det)
            print("dis_right:", dist)

def listener():
   rospy.init_node('camera_img', anonymous=True)

    # CompressedImage 라는 ROS 의 센서 메세지 형식을 사용하여 Topic Subscriber 를 완성한다.
    # Topic 이름은 시뮬레이터 Network 연결시 확인 가능하다.
   rospy.Subscriber('/radar_right',RadarDetections,radar_callback)    
   rospy.spin()

if __name__ == '__main__':
   print("gd")
   listener()