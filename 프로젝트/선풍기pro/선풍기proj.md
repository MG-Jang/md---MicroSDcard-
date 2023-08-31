# 선풍기 project

## 개요
1. 사용 부품
2. 작동 구성
3. 코드 구성

> 1. 사용 부품
   - DC 모터 x1
   - push switch x3 
   - 7segment LED x1
   - servomotor x1
> 2. 작동 구성
-   바람의 세기 구성은 3단계로 구별함.(0.6, 0.8, 1)
- switch는 각각 up, down, on/off 3개로 구성되어있다.
  - up: 세기를 올린다. 최대 1까지 상승
  - down: 세기를 내린다. 단 꺼지지는 않음
  - on/off: 꺼져있다면 1단으로 켜고 켜져있다면 0으로 만든다.
- 7segment: 현재 단수를 표현함
- servomotor 선풍기를 회전 시킴
> 코드 구성

```py
from gpiozero import PWMLED, LED, Button, AngularServo
from time import sleep

def show(n):
    for m in num[8]: m.off() #clear
    for m in num[n]: m.on() #show 

servo = AngularServo(5 ,min_angle =0, max_angle=180)

b_up = Button(6)
b_down = Button(13)
b_off = Button(19)
b_spin = Button(0)
fan = PWMLED(4)

g = LED(14)
f = LED(26)
a = LED(15)
b = LED(18)
e = LED(23)
d = LED(24)
c = LED(25)
DP = LED(8)
num = [[a, b, c, d, e, f], #0
    [b, c],#1
    [a, b, g, e, d], #2
    [a, b, g, c, d], #3
    [f, g, b, c], #4
    [a, f, g, c, d], #5
    [a, f, g, e, c, d], #6
    [f, a, b, c], #7 
    [a, b, c, d, e, f, g], #8
    [a, b, c, d, g, f]] #9

fan.value = 0
power = 0
show(power)
spin =0
while True:
    print(fan.value)
    #print(type(fan.value))
    if b_up.is_pressed:
        if fan.value == 0:
            fan.value =0.6
            power =1
            show(power)
        elif fan.value <= 0.8 :
            fan.value +=0.2
            power +=1
            show(power)
        sleep(0.3)
    if b_down.is_pressed:
        if fan.value >= 0.6:
            power-=1
            show(power)
            fan.value -=0.2
            sleep(0.3)
    if b_off.is_pressed:
        if fan.value == 0:
            power = 1
            show(power)
            fan.value = 0.6
        else :
            power = 0
            show(power)
            fan.value = 0
        sleep(0.3)
    if b_spin.is_pressed: 
        for i in range(180):
            print("angle",i)
            servo.angle = i
            sleep(0.02)
        for i in reversed(range(0,180)):
            print("angle",i)
            servo.angle = i
            sleep(0.02)   
        sleep(0.3)
        
```