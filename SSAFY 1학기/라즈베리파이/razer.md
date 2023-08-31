# 17번을 입력으로 사용

```py
from gpiozero import LED              
from time import sleep

lazer = LED(17)

while True:
    
    lazer.on()
    sleep(1)
    lazer.off()
    sleep(1) 
```