from gpiozero import LED, Button
from time import sleep
from signal import pause
def show(n):
    for m in num[8]: m.off() #clear
    for m in num[n]: m.on() #show number
def goal():
    lazer.on()
    for i in range(6):
        yellow.off()
        red.on()
        sleep(0.3)
        red.off()
        yellow.on()
        sleep(0.3)
    red.off()
    yellow.off()
    pause()

lazer = LED(17)  # Razer
button = Button(2)
red = LED(22)
yellow = LED(27)

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
#print("INPUT : ", end='')

while True:
    for i in range(1,10):
        show(i)
        sleep(1)
        if i == 7:
            if button.is_pressed:
                goal()
    sleep(0.5)
    for i in reversed(range(1,10)):
        show(i)
        sleep(1)
        if i == 7:
            if button.is_pressed:
                goal()
    sleep(0.5)
for m in num[8]: m.off()
#print("ha")
while True:
    sleep(1)
