from gpiozero import LED
from gpiozero import Button
from time import sleep

red = LED(17)
yellow = LED(27)

for i in range(5):
    yellow.off()
    red.on()
    sleep(0.2)
    yellow.on()
    red.off()
    sleep(0.2)
    
yellow.off()
red.off()