# ROS 환경 Py코드 기본 구조
ROS환경에서 작성되는 python코드는 공토적인 기본 구조를 가지고 있다.
아래 내용은 ROS Pub & Sub 정리에 있는 코드를 기반으로 작성 되었다.

##  -*- coding: utf-8 -*- & shebang라인 <hr>

py코드를 보면 가장 위에 흔히 볼 수 있는 내용. <br>
<span style="color:orange"> (주의!) <br>
<span style="color:orange"> 둘다 #이 앞에 있지만 주석이 아니므로 #까지 붙여야한다. <br>
<span style="color:orange"> 무조건 #!/usr/bin/env python 이 맨위에 존재해야한다.
```py 
#!/usr/bin/env python 
#-*- coding: utf-8 -*-  
```

- #!/usr/bin/env python 
    - 해당파일에 어떤 인터프리터를 사용할지 지정 <br>
    - 주석이 아니기 때문에 작성하자
    - 작성하지 않더라도 코드 자체에는 영향을 주지 않지만 아래와 같이 차이가 발생 
- #-*- coding: utf-8 -*-  
    - 한글 주석이 들어간 경우 필요.
```py
$ ./teacher.py # shebang이 있는 경우
$ python teacher.py # shebang이 없는 경우
```
- 버전을 구분해서도 작성이 가능
```py
#!/usr/bin/env python3
#!/usr/bin/env python2.6
...
``` 

<br>

## import , from , as <hr>

- import뒤에는 라이브러리
- from 뒤에는 모듈이 온다.
```py 
from std_msgs.msg import String
# std_msgs.msg 모듈에서 String 라이브러리 관련 부분만을 가져다 사용하겠다. 라는 의미
# 단 msg니깐 문자형만 존재한다면 X , Int32 처럼 정수형 실수형 등도 사용가능 
```
- as는 별명을 만들어준다.
```py 
import numpy as np
# numpy이름이 기니깐 np로 짧게 쓰겠다.(별명을 붙여준 느낌)
```
<br>

##  rospy <hr>

rospy란 ros의 파이썬 클라이언트 라이브러리이다.
- topic
- services
- parameter 등을 사용 가능
```py
# 추가 방법
import rospy
```
- rospy 라이브러리를 import
- import란 모듈,패키지,파이썬 표준 라이브러리를 사용

<br>

## rospy.init_node()  매우 중요! <hr>
노드의 이름, argument , anonymous 등 노드의 속성들을 결정하는 아주 중요한 요소 이다. <br>
함수를 간단히 살펴보면<br>
<span style="color:orange">def init_node (name , argv =none , anoymous = False , log_level = None ....)</span> <br>
과 같이 여러 요소들이 존재 하지만 필수 요소 중심으로 알아보자

- name: 해당 노드를 초기화하고 노드 이름을 설정 
```py
ex) rospy.init_node('teacher') # 노드 초기화 뒤 teacher로 이름 설정
```
<br>

## pub = rospy.Publisher('my_topic', String) <hr>

- my_topic이라는 이름의 topic을 publishing 하겠다는 publisher로 등록하는 부분
- 메세지 타입은 string을 담겠다.
- 나중에 내용을 전송할때는 아래와 같이 전송한다.
```py
pub.publish('call me please') #string으로 선언했으므로 이에 맞게 전달
```
<br>

## rate = rospy.Rate()<hr>
- 1초에 몇번 loop를 반복할지 rate라는 객체를 만드는 코드. <br>
ex) rate = rospy.Rate(2)라 하면
    - 1초에 2번 반복 = 0.5초에 한번씩 루프를 돌아야 한다.
    - 0.5초 짜리 타임슬롯을 생성
    - loop안에 있는 타임슬롯에 할당된 시간을 모두 소모한 후에 다시 loop를 반복
    <img src = "./img/rospy_rate.JPG">

## while not rospy.is_shutdown() <hr>

rospy.is_shutdown()이 true가 될때 까지 실행