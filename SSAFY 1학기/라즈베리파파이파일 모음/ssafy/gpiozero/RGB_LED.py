from gpiozero import PWMLED
from time import sleep

R = PWMLED(14)
G = PWMLED(15)
B = PWMLED(18)

while True:
    for i in range(10):
        R.value = i/10
        G.value = 0
        B.value = 0
        sleep(0.1)
    for i in range(10):
        R.value = 0
        G.value = i/10
        B.value = 0
        sleep(0.1)
    for i in range(10):
        R.value = 0
        G.value = 0
        B.value = i/10
        sleep(0.1)