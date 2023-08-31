# class 개념 이해하기

- 클래스, 객체, 인스턴스
- 클래스는 항상 대문자로 시작
- 객체는 소문자로 시작
- 객체의 개념과 인스턴스는 동일하다 생각하자



### class 기본<hr>
```py
# 클래스를 선언
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
         result = self.first + self.second
         return result

a = FourCal()
a.setdata(4, 2)
print(a.add())
```

- 클래스를 선언한다.
- a = FourCal() 로 a는 class FourCal을 사용가능
- a.setdata(4, 2) 로 self안에 first second를 넣는다.
- print(a.add()) 여기서 add는 아무것도 없는데 어떻게 출력되는지 궁금할꺼다
- 위의 a.setdata(4, 2)에서 self.first 와  self.second에 넣어주었다. 이를 사용하는것

### class 생성자<hr>
```py
# 클래스를 선언
class FourCal:
    def __init__(self, first, second):   # 생성자
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
         result = self.first + self.second
         return result

a = FourCal(5,3)
a.setdata(4, 2)
print(a.add())
```
- 생성자를 쓰는 이유는 만약 print(a.add())만을 사용하는경우 error가 발생한다. 왜?
- 왜냐하면 self안에 아무것도 없기 때문.
- 따라서 이를 방지하고자def __init__(self, first, second): 을 쓴후
- a = FourCal(5,3)처럼 a를 선언하는 순간 self값을 할당한다.

### Pyside를 예로들면 <hr>

```py
from PySide6.QtWidgets import *  
from PySide6.QtCore import *

class MyApp(QWidget):    #MyApp은 Qwidget의 자식
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        self.tm = QTimer()
        self.tm.setInterval(500)
        self.tm.timeout.connect(self.run)
        self.tm.start()


    def run(self):
        print("#", end = '')

app = QApplication()   
win = MyApp()  #win은 객체
win.show()
app.exec()
```

- app = QApplication()   # QApplication() 에 있는 모든 객체를 사용할 것이다.
- app은 객체가 된것
- win = MyApp()으로 만들면 win에서 MyApp에 있는 모든 것들을 사용 가능하다.
- ex) self.tm.timeout.connect(self.run) # 여기서 timeout이 객체
    - 참고 객체는 소문자로 이루어짐
- win.show() 에서show는 MyApp에 없지 않나? 라고 생각 할 수 있다. 하지만 MyApp은 QWidget의 자식 이기때문에 QWidget에 있는 show를 가져다 쓴 것이다.