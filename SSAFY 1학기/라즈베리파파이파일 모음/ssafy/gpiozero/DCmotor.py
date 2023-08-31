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
        
