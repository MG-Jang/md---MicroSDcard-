from gpiozero import LED              
from time import sleep

lazer = LED(15)

while True:
    
    lazer.on()
    sleep(1)
    lazer.off()
    sleep(1) 