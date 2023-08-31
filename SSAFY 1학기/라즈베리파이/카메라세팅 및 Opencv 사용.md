# 라즈베리파이 카메라

- 아래 작성글은 카메라가 리본케이블로 연결된 경우를 뜻함

## 기본세팅 <hr>

- 카메라를 사용가능하도록 설정해준다.
```
$ sudo raspi-config 
```
이후
1. Interfacing Optinons 에들어가서 
2. camera를 enable 상태로 변경
3. reboot
4. 잘안되면 인터넷 검색

## 사진 찍기<hr>

- test.jpg로 사진이 생성, 해상도는 카메라가 가진 최고 resolution으로 찍힘
```
$ raspistill -o test.jpg 
$ raspistill -o test.jpg -vf   # 상하 반전이일어남
$ raspistill -o test.jpg -hf   # 좌우 반전이일어남
```
## 동영상 촬영하기<hr>
```
$ sudo apt-get update
$ sudo apt-get install python-picamera
$ sudo rpi-update
``` 

raspivid -t 10000 -o video.h264 -f  실행

 sudo apt-get install gcc g++ cmake libjpeg8-dev
 git clone https://github.com/jacksonliam/mjpg-streamer.git

 > 라즈베리 파이 영상 실시간 스트리밍 방법 1
 ```
$ sudo apt-get install gcc g++ cmake libjpeg8-dev
$ git clone https://github.com/jacksonliam/mjpg-streamer.git

# 소스파일에 이동
$ cd mjpg-streamer/mjpg-streamer-experimental

# 컴파일
$ make distclean
$ make CMAKE_BUILD_TYPE=Debug   # 여기서 문제 발생
$ sudo make install
```

> 라즈베리 파이 영상 실시간 스트리밍 방법2

```
$ pip install pyzmq
```

> 영상 스트리밍을 하지 않고 라즈베리 파이 자체적으로 판단. (성공)
- 참고 사이트: https://seo-dh-elec.tistory.com/32

```
 $ sudo apt-get update
 $ sudo apt-get upgrade
 $ git clone https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.git
$ mv TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/ tflite1
```

open Cv를 설치 한다.
```
~ $ cd tflite1
~/tflite1 $ sudo pip3 install virtualenv
~/tflite1 $ python3 -m venv tflite1-env
~/tflite1 $ source tflite1-env/bin/activate
(tflite1-env)~/tflite1 $ bash get_pi_requirements.sh
```

<span style="color:orange">디렉토리를 이동시킨다.</span> 항상 터미널을 다시 시작하면 실행시켜줘야함
```
$ cd tflite1
$ source tflite1-env/bin/activate
(tflite1-env)~/tflite1 $    #이런 형태로 터미널 환경이 설정된 상태로 아래 실행
```

물체 인식 실행
```
$ python3 TFLite_detection_webcam.py --modeldir=TFLite_model
```
- 가상환경 나가기
```
$ deactivate
```

- 가상환경에서 실행하는 경유 no mobules smbus 라 뜬다. 이를 해결하고자 아래 코드를 실행한다.
```
$ pip install smbus
```

> 가상환경 관련 자료
https://velog.io/@kyle13/Python-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-venv