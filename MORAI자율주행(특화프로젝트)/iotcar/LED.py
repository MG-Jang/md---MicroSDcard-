from gpiozero import LED
from time import sleep
import mysql.connector as mariadb

yr1 = LED(11) # yellow_right
yr2 = LED(5)
yr3 = LED(6)
yr4 = LED(19)
yr5 = LED(26)
yl1 = LED(7)   # yellow_left
yl2 = LED(12)
yl3 = LED(16)
yl4 = LED(20)
yl5 = LED(21)
fr = LED(2) #front  
br = LED(3) # back

# led_signal 0=아무것도x, 1 = left , 2 = right, 3= caution

fr.on() # 전방은 항상켜짐
while True:
  #red.on()
  print("command")
  command = input()
  if(command == 'r'):
    for i in range(2):
      yr1.on()
      sleep(0.1)
      yr2.on()
      sleep(0.1)
      yr3.on()
      sleep(0.1)
      yr4.on()
      sleep(0.1)
      yr5.on()
      sleep(0.1)
      yr1.off()
      yr2.off()
      yr3.off()
      yr4.off()
      yr5.off()
      sleep(0.1)
  elif(command == 'l'):
    for i in range(2):
      yl1.on()
      sleep(0.1)
      yl2.on()
      sleep(0.1)
      yl3.on()
      sleep(0.1)
      yl4.on()
      sleep(0.1)
      yl5.on()
      sleep(0.1)
      yl1.off()
      yl2.off()
      yl3.off()
      yl4.off()
      yl5.off()
      sleep(0.1)
  elif(command == 'a'):
    for i in range(2):
      yr1.on()
      yr2.on()
      yr3.on()
      yr4.on()
      yr5.on()
      yl1.on()
      yl2.on()
      yl3.on()
      yl4.on()
      yl5.on()
      sleep(0.25)
      yl1.off()
      yl2.off()
      yl3.off()
      yl4.off()
      yl5.off()
      yr1.off()
      yr2.off()
      yr3.off()
      yr4.off()
      yr5.off()
      sleep(0.25)
  elif(command == 'fo'):
    fr.on()
  elif(command == 'ff'):
    fr.off()
  elif(command == 'bo'):
    br.on()
  elif(command == 'bf'):
    br.off()

  #br.on()
  # fr.on()
  # sleep(2)
  # #br.off()
  # fr.off()
  # sleep(2)

  #br.on()