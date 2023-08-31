# 7 segment 

- 7segnment는 사실 7개가 아니라 8개의 LED를 가지고 있음(점 포함)


```py
from gpiozero import LED
from time import sleep
def show(n):
    for m in num[8]: m.off() #clear
    for m in num[n]: m.on() #show number

# pin number
g = LED(14)
f = LED(26)
a = LED(15)
b = LED(18)
e = LED(23)
d = LED(24)
c = LED(25)
DP = LED(8)
num = [[a, b, c, d, e, f], #0
    [b, c],#1
    [a, b, g, e, d], #2
    [a, b, g, c, d], #3
    [f, g, b, c], #4
    [a, f, g, c, d], #5
    [a, f, g, e, c, d], #6
    [f, a, b, c], #7 
    [a, b, c, d, e, f, g], #8
    [a, b, c, d, g, f]] #9
print("INPUT : ", end='')
n = int(input())
a = n // 10000 %10
print(a)
b = n // 1000 % 10
c = n // 100 % 10
d = n // 10 % 10
e = n // 1 % 10
print(b)
print(c)
print(d)
print(e)
lst = [a, b, c, d, e]
for i in range(5):
    show(lst[i])
    sleep(0.5)

while True:
    sleep(1)

```