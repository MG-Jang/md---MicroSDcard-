from gpiozero import AngularServo
from time import sleep

servo = AngularServo(5 ,min_angle =0, max_angle=180)

for i in range(180):
    print("angle",i)
    servo.angle = i
    sleep(0.02)
for i in reversed(range(0,180)):
    print(i)
    servo.angle = i
    sleep(0.02)
servo.angle =0