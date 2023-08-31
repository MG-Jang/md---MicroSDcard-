"""
from gpiozero import Button
from time import sleep

button = Button(18)

while True:
	if button.is_pressed:
		print("Button is pressed")
	else:
		print("Button is not pressed")
	sleep(0.1)
"""	
from gpiozero import Button                  
from time import sleep                      

button = Button(18)                             
cnt = 0
while True:
    cnt+=1
    print(button.is_pressed)
    print(cnt)
    if button.is_pressed:                    
        print("Button is pressed")          
        sleep(1)
    else:                                   
        print("Button is not pressed")       
        sleep(1)              
     #print("running")
