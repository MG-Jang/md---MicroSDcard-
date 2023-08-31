from gpiozero import Button
from signal import pause

cnt = 0 

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

button = Button(2)

cnt +=1
print(cnt)
button.when_pressed = say_hello
button.when_released = say_goodbye

pause()