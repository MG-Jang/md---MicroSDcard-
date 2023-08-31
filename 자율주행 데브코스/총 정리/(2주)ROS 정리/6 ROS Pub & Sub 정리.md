# ROS Publisher & Subscriber

ROS통신에는 2개의 node가 Publisher(발행자) 와 Subscriber(구독자)를 만들어 Topic을 이용해 정보를 주고 받는다. 아래 내용을 통해 어떤식으로 주고 받는지 확인해보자. 

## Pub & Sub 주요 특징 <hr>

||Publisher|Subscriber|
|---|---|---|
|노드생성|rospy.init_node('node_name')|rospy.init_node('node_name')|
|선언문|pub = ros.Publisher('topic이름', 자료형)|sub = rospy.Subscriber('topic이름',자료형,callback)|
|전송주기|rate = rospy.Rate(숫자)|필요x(항시 받을 준비)|
|출력문|보내는 node임에 필요x|def callback(msg):|
|반복문|while문|spin문|
## Sub Pub 예제 코드 <hr>

위 내용을 참고하여 teacher.py(publisher) -> student.py(subscriber)를 제작

> teacher.py 
```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 해당파일에 어떤 인터프리터를 사용할지 지정,(주석이 아니기 때문에 꼭 작성하자)

import rospy # 노드 생성에 필요한 함수를 호출
from std_msgs.msg import String
# 필요한 메시지 형식인 String import 하기

rospy.init_node('teacher')
# teacher라는 이름으로 노드를 초기설정

pub = rospy.Publisher('my_topic', String)
# my_topic이라는 토픽을 발행하는 퍼블리시 노드 생성

rate = rospy.Rate(2)
# 1초에 2번씩 토픽을 발행하도록 설정, Hz

while not rospy.is_shutdown():
# rospy.is_shutdown()이 true가 될때 까지 실행
    pub.publish('call me please')
# "call me please"이라는 메시지를 my_topic으로 발행
    rate.sleep()
# 위 rate 에서 설정한 0.5초 주기로 while문이 실행 되도돌 해줌
# 만약 sleep 문이 없다면 0.5초동안 pub.publish가 미친듯이 반복된다.
```

> student.py 
```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 파이썬 환경 설정

import rospy
# 노드 생성에 필요한 함수를 호출
from std_msgs.msg import String
# 필요한 메시지 형식인 String import 하기

def callback(msg):
# callback이라는 이름의 함수를 정의
    print msg.data
# 받은 메시지의 데이터를 print함
    
rospy.init_node('student')
# student라는 이름으로 노드를 초기설정
sub = rospy.Subscriber('my_topic', String, callback)
# my_topic이라는 토픽을 구독하는 Subscriber를 생성
# topic을 받는 subscriber 
# 받고자하는 topic은 my_topic
# topic에 담긴 내용은 string 형식
# topic이 올때 마다 callback 함수를 실행
rospy.spin()
# shutdown이 될때까지 무한 루프를 돌린다.
```