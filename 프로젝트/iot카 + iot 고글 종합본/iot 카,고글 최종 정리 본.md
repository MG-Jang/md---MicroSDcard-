# iot 카 고글 최종 정리본.

<span style="color:orange">주의!! 다음 내용에는 AWS 주소 값이 들어있기 떄문에 git에 올리는 경우 주소와 관련된 내용은 다 내려야 한다. </span>

- 다음 사이트를 참고하자
https://splashy-zinnia-879.notion.site/IoT-RC-Car-bc5b37d933d34e68b3dcbce23eda3d7d

- Mysqul 설치에 관한 내용은 "DB_SSAFY_Day1" 참고 하자

- 내 AWS: host, user , pas, data 정보
  - host: 13.125.137.101
  - user: jang
  - pas: 1234
  - data: jangDB


## Query 코드 넣기 내 host, user , pas, data 로 변경 하였다. 
```py
from PySide6.QtWidgets import *
from mainUI import Ui_MainWindow
import mysql.connector

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        self.db = mysql.connector.connect(host='13.125.137.101', user='jang', password='1234', database='jangDB')
        self.cur = self.db.cursor()


    def start(self):
        self.cur.execute("select * from command")
        for (id, time, cmd_string, arg_string, is_finish) in self.cur:
            print(id, time, cmd_string, arg_string, is_finish)

    def closeEvent(self, event):
        self.cur.close()
        self.db.close()

app = QApplication()
win = MyApp()
win.show()
app.exec()
```

## QTimer로 반복적으로 Query 하기 (현재 오류 발생)-> 

- 해결: 문제점 LogText 창이름을 정확하게 설정하지 않음.

```py
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from mainUI import Ui_MainWindow
import mysql.connector

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init()

    def init(self):
        self.db = mysql.connector.connect(host='13.125.137.101', user='jang', password='1234', database='jangDB')
        self.cur = self.db.cursor()

        #timer setting
        self.timer = QTimer()
        self.timer.setInterval(500) #500ms
        self.timer.timeout.connect(self.pollingQuery)

    def start(self):
        self.timer.start()

    def pollingQuery(self):
        self.cur.execute("select * from command")
        self.ui.logText.clear()
        for (id, time, cmd_string, arg_string, is_finish) in self.cur:
            str = "%d | %s | %6s | %6s | %4d" % (id, time.strftime("%Y%m%d %H:%M:%S"), cmd_string, arg_string, is_finish)
            self.ui.logText.appendPlainText(str)

    def closeEvent(self, event):
        self.cur.close()
        self.db.close()

app = QApplication()
win = MyApp()
win.show()
app.exec()
```

## mobaxterm 에서 python3로 실행시 error 발생
1. reboot 후 다시 동작시켜보기
2. 센서가 정상적으로 연결되었는지 확인
3. VNC로 접속하여 thony를 이용하여 실행

> test 코드
1. 1초간 왼쪽으로 전진
2. 1초간 오른쪽으로 전진
3. 1초간 왼쪽으로 후진
4. 1초간 오른쪽으로 후진
5. 바퀴를 좌우로 이동
6. 1번부터 다시 무한 루프를 돔

```
myMotor = mh.getMotor(2)

myMotor.setSpeed(150)
myMotor.run(Raspi_MotorHAT.FORWARD)
time.sleep(1)

myMotor.setSpeed(150)
myMotor.run(Raspi_MotorHAT.BACKWARD)
time.sleep(1)

myMotor.setSpeed(150)
myMotor.run(Raspi_MotorHAT.RELEASE)
time.sleep(1)
```

> 4. iot RCCar 개발 설명
- MotorHat이 없는 경우

```
$ cd ~/bbqcar  # 굳이 안하고 자신이 원하는 폴더에 해도됨
$ wget http://raspberrypiwiki.com/images/a/ac/Raspi-MotorHAT-python3.zip --no-check-certificate
$ unzip ./Raspi-MotorHAT-python3.zip
```
$ deactivate  #가상환견 나가기

- mysqul을 켜서 서버가 정상적으로 작동하고 있는지 확인한다.
- command 받기 내용을 차량에 넣는 app.py 내용을 말하는 것이다.