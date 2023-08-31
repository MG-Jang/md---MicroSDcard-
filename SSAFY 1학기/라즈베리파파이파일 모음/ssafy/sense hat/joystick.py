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