# GUI 개발 정리

### 기본개념 <hr>

차량 또는 산업에서 그래픽 적으로 나타내는 것들
- ex) 차량 계기판 , 세탁기 GUI 등등
<br>
<br>

> 임베디드 Linux 에서 GUI

Qt가 가장 많이 사용됨. 
- C++ 기반이다. (python으로도 구동가능)
- Windows, Linux, MacOS, Android, VxWorks, Tizen 지원
- 네트워크 , 그래픽 , DB, OpenGL 등 쉬운 API 지원

> Qt Creator(현대 오토에버사용)
- Qt 의 대표적인 IDE 이고 GPL 이다
- Editor Qt Quick Designer Qt Designer 모두 포함
- 디버깅 / SVC / 크로스 컴파일 / 가상 에뮬레이터도 추가

### Pyside준비 <hr>

> pyside 다운로드
 - https://download.qt.io/official_releases/QtForPython
 - file -> settings -> project:이름 -> project interpreter -> 우측 + 버튼 
 - pyside6만 설치
 - ![캡처](/img/pyside6_venv%EC%84%A4%EC%B9%98.JPG)
 - install Package

### Pyside기본 구조 <hr>

```py
from PySide6.QtWidgets import * 
# 여기서 import *을 하는 이유: 변수 / 함수 대신 * 적으면 모두 가져 옴
# import *을 하지 않으면 항상 모듈 명을 적어줘야함

app = QApplication()   #하나의 instance 생성 + QApplication()안에 있는 객체를 사용할것이다.
win = QWidget()
win.show() # win으로 구성된것을 window에 띄어줄때 사용
app.exec() # 무한루프를 돌림, eventlistener 
```

> QLabel (출력을 위해 사용)
- Qt 의 기본 Label Class 중 하나
- Show 를 할 때 Window 가 출력 됨

```py 
from PySide6.QtWidgets import *

app = QApplication()
label = QLabel("hello")
label.show()
app.exec()
```

### Class로 widget상속받기 <hr>
- class md파일 참고할것


### Qt Desinger.exe 실행

1. 디자이너를 실행
2. 디자인을 한다.
3. 다른 이름으로 저장을 눌러 hi 파일로 해당 project 폴더로 경로를 바꾼후 저장
4. 예를 들어 ui 파일이름을 hi로 저장했다면 이를 다시 파이썬파일로 변경해야함
5. pyside6-uic.exe hi.ui -o hi_ui.py
6. hi.ui파일이 py파일로 변경