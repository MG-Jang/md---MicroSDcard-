from gpiozero import Button                  
from time import sleep
from signal import pause
  
button = Button(2)                             
cnt = 0
if button.wait_for_press():
    print("hi")
#elif button.is_released:
#    print("say_goodbye")

pause()


"""
while True:
    #print(button.is_pressed)
    #print(cnt)
    sleep(0.2)
    if button.is_pressed:                    
        #print("Button is pressed")          
        cnt +=1
        print(cnt)
        while True:
            print("HA")
            if button.when_released:
                print("HI")
                break
            
        
    #else:                                   
        #print("Button is not pressed")       
        #sleep(1)
"""
        