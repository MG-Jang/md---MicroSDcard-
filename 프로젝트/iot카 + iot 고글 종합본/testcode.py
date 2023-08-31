from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(21,20) # Echo, Trig

while True:
    print(sensor.distance, "m")
    sleep(0.1)
