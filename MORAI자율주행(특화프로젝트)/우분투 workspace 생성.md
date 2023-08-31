- 설치 명령어
```py
$ cd ~/
#워크스페이스 생성
$ mkdir –p catkin_ws/src
$ cd catkin_ws
$ catkin_make

# 패키지 생성 및 빌드
$ cd ~/
$ cd catkin_ws/src
$ catkin_create_pkg beginner_tutorials rospy std_msgs
$ cd beginner_tutorials && mkdir scripts
$ cd ~/catkin_ws
# 꼭 catkin_ws에서 실행
$ catkin_make

# catkin 환경 변수 선언
$ source ~/catkin_ws/devel/setup.bash
#패키지 재구축 
$ rospack profile
```

설치가 끝났다면 아래 그림과 같이 폴더가 생성 된 것을 확인 할 수 있다.
- $ cd /catkin_ws/src/beginner_tutorials
![캡처](/img/beginner_tutorials.JPG)


```py
#!만약 아래의 명령어 실행시  unable to resolve host address ‘raw.github.com’ 라는 오류 문구가 뜸. 따라서 t7/ssafy/특화프로젝트/py파일 모음 폴더 안에 넣어둔 talker.py를 가져다가 복붙 또는 파일이동으로 해서 수동으로 넣어주자 
beginner_tutorials/scripts 폴더 안에 talker.py 다운로드
$ cd ~
$ cd ~/catkin_ws/src/beginner_tutorials/scripts/
$ wget https://raw.github.com/ros/ros_tutorials/melodic-devel/rospy_tutorials/001_talker_listener/talker.py
# wget은 web get의 약어로 웹사이트에서 가져올때 많이 사용된다.
```