# IoT RC 카 만들기

1. 목표
2. 사용 부품
3. 사용 프로그램


> 1. 목표
- 주어진 킷트를 조립하여 rc-car를 제작한다.
- Raspberry pi 4 model B 를 컨트롤러로 사용하여 ssh로 연결된 호스트컴퓨터(pc)에서 콘솔에 명령어를 입력함으로
써 차량을 제어할 수 있다.
- 구현해야할 기본 명령은 '앞으로/ 뒤로/ 정지/ 빠르게/ 느리게/ 오른쪽/ 왼쪽/ 중앙' 이다.
- wifi통해 네트워크 연결되도록 한다.
- PWM 개념을 이해하고 이를 Servo Motor 에 적용해본다.
> 2. 사용 부품
- 모터: 감속기와 영구자석으로 구성된 모터
- servo motor: 180도 안에서 축의 위치를 설정(방향을 결정하는데 사용)
- 배터리 18650:
  - 18650규격에 3.6V 2600mAh 배터리 3개 직렬 연결 사용
- 전원 공급 모듈(DC 5A): 
  - 배터리 팩에서 출력되는 12V를 라즈베리파이와 모터 컨트롤러에 부착,9~36V  전압을 라즈베리파에 맞게 5V,5A 로 스탭 다운
  
<img src="~/../../img/전원%20공급%20모듈.jpg"  width="200" height="100">

- 라즈베리파이: 
  - 주 MCU

<img src="~/../../img/raspberry4.jpg"  width="200" height="100">

- 모터 컨트롤러: 
  - i2c기반의 모터 컨트롤러
  - 최대4개의 DC모터, 2개의 servo 모터 연결가능(M1,M2,M3,M4) 나의 경우 M2 연결
  - 256단계의 speed제어가 가능, 각 모터당 공급가능한 전류 1.2A, 최대 3A 가능
  - 모터에 GPIO만으로는 전압 공급이 원할하지 않기 때문에 별도의 전압을 공급받기위해 사용, servo 모터 DC모터 전원공급
  - 
<img src="~/../../img/stepper%20motor.jpg"  width="200" height="150">

> 라즈베리파이 환경 설정
- 먼저 VNC와 I2C를 사용할 것이므로 config에서 활성화 해준다.
- I2C 유틸리티 설치: (I2C가 잘연결되었는지 확인)
  - sudo apt-get install python-smbus i2c-tools
  - sudo i2cdetect -y 1
  - 위의 명령어를 입력한경우 70, 6f(0x70, 0x6f 주소를 의미) 가 연결된것을 볼 수 있다. DC, servo 모터 2개
-  motot HAT라이브러리 다운로드:
   -  wget http://wiki.geekworm.com/images/a/ac/Raspi-MotorHAT-python3.zip
   -  unzip Raspi-MotorHAT-python3.zip
- 홈으로 파일 움기기
  - $ cd Raspi-MotorHAT-python3
  - $ cp Raspi_* ~/
    - 위 명령어를 실행하면 Raspi-MotorHAT-python3폴더에 있는 파일중 Raspi로 시작하는 파일들을 홈으로 가져온다. 
    - 굳이 홈디렉토리가 아니여도 되지만 난 홈에서 작업을 할거다. (따로 폴더를 만들어도됨)
    - 라이브러리 3개 파일(Raspi_MotorHAT.py, Raspi_PWM_Servo_Driver.py, Raspi_I2C.py)을 현재 작업디렉토리에 넣
어둔다.

> 모터 움직이기

- 홈파일에 test.py 파일을 생성후 Thonny를 이용하여 실행
  - 만약 홈파일에 생성하지 않고 다른 폴더에 생성하고 싶다면 위의 cp Raspi_* ~/ 와 같은 명령어를 이용해서 해당폴더에 위와 동일한 3개의 파일을 넣어야함 

 ## DC 모터<hr/>
```py
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from time import sleep
mh = Raspi_MotorHAT(addr=0x6f)  # addrss
myMotor = mh.getMotor(2) # M2 connect  
myMotor.setSpeed(150) # speed 150, Topspeed 255
myMotor.run(Raspi_MotorHAT.FORWARD)  
sleep(10) #10sec
myMotor.run(Raspi_MotorHAT.RELEASE)
```
- 코드 설명
  - 150의 속도로 10초간 운행후 종료 (최대 255 까지 속도 조절 가능)
  - 주소 확인은 위의 sudo i2cdetect -y 1 통해 확인. 현재는 0x6f

- 참고: 
  - pdf 의 4번줄 moter가 오타, 
  - 라이브러리를 확인하고 싶다면 Raspi_MotorHAT에 들어가보자

 ## Servo Motor <hr/>


- <span style="color:orange">주의!!!!!</span>
  - 꼭 서보 모터 test시 차축과 연결을 해제 하고 할것
  - 안그러면 최대 각도로 움직이면서 차량에 손상을 줌
  - <span style="color:orange">현재는 #0에 서보모터가 연결되어있음 going test를 할때는 #1으로 변경할것</span>
```py
from Raspi_MotorHAT import Raspi_MotorHAT
from time import sleep
mh = Raspi_MotorHAT(0x6F) # motor-HAT i2c
servo = mh._pwm
servo.setPWMFreq(60)  # 60 Hz
while (True):
  servo.setPWM(1, 0, 300)  # (pin 1, on ,off)
  sleep(1)
  servo.setPWM(1, 0, 407)
  sleep(1)
  servo.setPWM(1, 0, 500)
  sleep(1)
  servo.setPWM(1, 0, 407)
  sleep(1)
```
- <span style="color:orange">PWM</span> 사용
  - 개념: 일정 주기로 plus를 생성한다. 예) LED 밝기 조절
  - Servo 역시 Pulse 폭에 따라 특정 각도로 움직인다.
  - 모터 컨트롤러에서 입력값에 따라 알아서 주기와 10설정해줌
  - 우리가 사용하는 컨트롤러는 4096 등분이 가능 하다.
    - ex) (0,2048) 이면 50%, (0,410) 10% 이다.
  - 우리가 사용하는 servo는 60hz인 경우 10% 듀티일때 중립. 5% 최소 15% 최대<br><span style="color:orange">(서보모터의 듀티를 5~15% 범위가 아니라면 고장남)</span>

- 코드 설명
  - 서보 컨트롤러 오브젝트 앞서 'mh = Raspi_MotorHAT(0x6F)' 문장에서 Raspi_MotorHAT object를 만드는 순간 내부적으로 이미 서보 컨트롤러 오브젝트를 mh._pwm라는 이름으로 사용할 수 있다.
  - servo.setPWM(0, 0, 407) #(장치번호,on,off)
    - 첫번째는 장치번호
    - on,off 의미 
    - 위의 예시를 참고하면 0초에 시작해서 407초에 끈다는 뜻
      - 즉 407ms 만큼 펄스를 보냄(PWM 개념) 
      - 200ms : 0도 
      - 407 : 90도
      - 614 : 180도  
> 주행 테스트
```
test_going ㅅ
```


> 기타 정리
- 참고: 서보모터 나중에 풀수 있어서 풀림 방지 너트를 살짝 해둠

- sd 뒷면 코드 0505.. 를 사용
- ip address는 ip sancer를 이용하여 70:5D:CC:FE:48:31 MAC주소 탐색(뒤의 와이파이 중계기 코드)
- 참고: 모델 MAC 주소는 e45f01262eba 
- 비번 178912mg#
  - #을쓰면 일단 오류나서 보류 -> # 추가함.  

172.30.1.14