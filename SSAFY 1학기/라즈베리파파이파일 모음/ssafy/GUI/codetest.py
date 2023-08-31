from gpiozero import LED, Button, AngularServo
from signal import pause
from time import *

def go():
    LED1.on()
    LED2.off()
    
def ho():
    LED1.off()
    LED2.on()
    
LED1 = LED(16)
LED2 = LED(20)
servo = AngularServo(21, min_angle =0 , max_angle =90 )
btn = Button(2)

for i in range(0,90,15):
    servo.angle = i
    sleep(0.5)
    
btn.when_pressed = go
btn.when_released = ho

pause()