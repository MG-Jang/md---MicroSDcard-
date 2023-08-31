# 기본 GPIO를 기본으로 함

- GPIO를 기본으로 작동됨.
- LED를 연결시 저항을 꼭 추가하자
- GND 신경써서 연결

> LED 작동
- GPIO 17번 , GPIO 27번 LED 작동 
```py
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
```

> button 작동

- GPIO 18핀에 연결
- 버튼의 경우 단순히 전류가 흐르면 연결되는것은 아닌듯.
- button.is_pressed 버튼이 눌렸는지 측정 
```py
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
```

- 버튼이 눌러질때까지 대기
```py
if button.wait_for_press():
    print("hi")
```