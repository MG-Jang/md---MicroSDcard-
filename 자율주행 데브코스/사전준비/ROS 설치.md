# ROS 설치

참고사이트: http://wiki.ros.org/melodic/Installation/Ubuntu

```py
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

$ cat /etc/apt/sources.list.d/ros-latest.list
$ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
# !!! 만약 위 코드가 error가 생긴다면==================================
$ sudo apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
#================================================================
$ sudo apt-get update
$ sudo apt install ros-melodic-desktop-full
# 쉘 환경 설정
$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
# 필수도구 설치
$ sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
# rosdep 초기화
$ sudo rosdep init
$ rosdep update

# 설치 확인
$ roscore 
$ rosnode list # 새로운 터미널하나 열어서 실행 할 것 
```

- ROS workspace 
ROS 구동을 위해서는 ws(workspace)가 필요하다.
```py
$ cd #home으로 이동
$ mkdir -p ~/xycar_ws/src #서브폴더 생성
$ cd xycar_ws
$ catkin_make # ROS 코딩 환경 셋업과 정리
```
* 참고사항:
catkin_make란 빌드명령어로 ROS 프로그램과 관련있는 모든 것들을 정리하여 최신 상태로 만드는 작업. 

- ROS 작업 환경변수 설정
```py
$ cd 
$ sudo gedit ~/.bashrc # .bashrc 파일이 나오는데 이때 아래 내용을 맨 밑에 추가
#==============================bashrc
alias cm='cd ~/xycar_ws && catkin_make'
alias cs='cd ~/xycar_ws/src'

source /opt/ros/melodic/setup.bash
source ~/xycar_ws/devel/setup.bash
export ROS_MASTER_URI=http://localhost:11311
export ROS_HOSTNAME=localhost
#=====================================
$ source .bashrc 
```
- 설치 확인
```py
$ printenv | grep ROS
```
- 아래와 같이 나오면 정상
```
ROS_ETC_DIR=/opt/ros/melodic/etc/ros
ROS_ROOT=/opt/ros/melodic/share/ros
ROS_MASTER_URI=http://localhost:11311
ROS_VERSION=1
ROS_PYTHON_VERSION=2
ROS_PACKAGE_PATH=/home/mg/xycar_ws/src:/opt/ros/melodic/share
ROSLISP_PACKAGE_DIRECTORIES=/home/mg/xycar_ws/devel/share/common-lisp
ROS_HOSTNAME=localhost
ROS_DISTRO=melodic
```
