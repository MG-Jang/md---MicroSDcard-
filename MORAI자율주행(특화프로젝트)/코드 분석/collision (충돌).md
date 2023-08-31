#  장애물 충돌 데이터 받기

장애물과 충돌한경우 리눅스 환경에서 데이터를 받아온다. 이를 위해서 ROS Bridge를 실행하여 MORAI 와 우분투를 서로 연결시켜준다.

> ROS Bridge 세팅 

 ROS 와 시뮬레이터를 연동시 ROS Bridge 라는 개념을 사용한다. 
- ROS 개발 환경 구축

```py
$ cd ~/catkin_ws/src

# simulator ROS message
$ git clone https://github.com/morai-developergroup/morai_msgs.git

#git clone을 사용 할 수 없는 경우
$ sudo apt-get install git

```

## 시뮬레이터와 ROS연동

<br>

ROS는 원래 리눅스 환경에서 작동된다. 하지만 우리의 노트북은 윈도우 환경이기 때문에 VM을 이용해서 리눅스 가상환경을 만들어 준 후 사용한다.

<img src="https://github.com/MG-Jang/img/blob/main/ros-simulator.JPG?raw=tru"  width="500" height="300">

```py
# Rosbridge 실행
$ roslaunch rosbridge_server rosbridge_websocket.launch
```

- MORAI ROS 네트워크 설정

<img src="https://github.com/MG-Jang/img/blob/main/ros-morai-network-setting.JPG?raw=true"  width="500" height="300">

```py
# 우분투 터미널에서 입력
$ ifconfig
```


```py
# 충돌데이터 입력
$ rostopic echo /CollisionData
```