# sense_hat

> 시작
- sudo apt-get install python3-sense-emu sense-emu-tools  : 에뮬레이터 설치 
- from sense_hat 을 사용하면  실제 동작
- form sense_emue를 사용하면 가상에서 동작



|자주사용되는 명령어||
|---|---|
|sense.clear()|전체 끄기|
|sense.show_letter(str[i])|단어 한개씩 출력|
|sense.show_message("hi")| 문장 출력|
|||

### 색상
```py
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (160, 32, 240)
```


> 문장 출력하기

```py
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.show_message("jang Myoung geun")
```

>  map 만들기

```py
from sense_hat import SenseHat
import time

sense = SenseHat()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

map = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
    ]

sense.set_pixels(map)

```

> 자이로 기능 이용

```py
from sense_hat import SenseHat
from time import sleep

sense =SenseHat()

while True:
    ori = sense.get_orientation_degrees()
    print(f'[{ori["pitch"]: 5.1f}] - ', end = '')
    print(f'[{ori["roll"]: 5.1f}] - ', end = '')
    print(f'[{ori["yaw"]: 5.1f}]', end = '')
    print()
```

> 빛세기 조절
```py
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear(255,255,255)
sense.low_light = True
time.sleep(2)
```

> 조이스틱 (이벤트 발생까지 대기)
```py
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    event = sense.stick.wait_for_event()
    print("{}{}".format(event.action, event.direction))
    sleep(0.4)
```

>조이스틱 (이벤트 발생까지 대기x) 폴링 방식
```py
from sense_hat import SenseHat
from time import sleep
T = [80,0,130]
sense = SenseHat()
tx = 0
ty = 0 
sense.clear()
sense.set_pixel(tx,ty,T)
while True:
    for event in sense.stick.get_events():
        print("HELLO {} {}".format(event.action, event.direction))
        if (event.direction == "right") & (event.action == "pressed"):
            print("hi")
            tx +=1
        if (event.direction == "left") & (event.action == "pressed"):
            tx -=1
        if (event.direction == "down") & (event.action == "pressed"):
            print("hi")
            ty +=1
        if (event.direction == "up") & (event.action == "pressed"):
            tx -=1
        sense.set_pixel(tx,ty,T)
        sleep(1)
    print("hi")

```