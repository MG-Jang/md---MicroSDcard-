# 우분투 git clone 및 ROS 연동

우분투 환경에서 git 내용을 clone 할 경우 순서를 설명해 두었다. <br>
아래 내용을 한가지 예시를 참고하여 설명하였다. <br>
설치 이후 ROS 연동 방법까지 서술 하였다.

```py
# 1. git 에서 clone을 딴다. (이때 https 형태로 복사)
# 2. 우분투 터미널에서 git clone을 실행. (참고: git clone 기능이 설치가 안되어 있다면 설치먼저 할 것)
$ git clone https://lab.ssafy.com/instruction/7th/skeleton-projects/mobility-autodriving-skeleton-git
# 3. 다운로드 받은 폴더중 사용할 코드가 들어있는 폴더를 catkin_ws/src로 가져온다.아래의 경우 mv를 사용하여 폴더 위치를 변경.
ssafy@ssafy-VirtualBox:~/catkin_ws/src/mobility-autodriving-skeleton/ssafy_ad$ mv ssafy_1 ./../..
# 4. catkin_make 실행
$ catkin_make
# 4-1.만약 정상적으로 작동하지 않는다면 clean 후 다시 위 make 명령어 입력
$ catkin_make clean 

#5. 설치가 모두 끝났다면 아래 명령어를 실행 (환경 변수 및 패키지 실행) 아래 2개 명령어는 터미널 열때마다 실행
$ source ~/catkin_ws/devel/setup.bash
$ rospack profile

# roscd를 사용해서 폴더를 들어간다.
$ roscd ssafy_1/scripts
$ chmod +x my_name_talker.py #사용할 py 파일 이름을 입력, 코드의 실행권한을 주는 것임으로 한번만 주면 다음부터는 굳이 입력할 필요는 없다.
$ rosrun ssafy_1 my_name_talker.py # 코드 실행



```
