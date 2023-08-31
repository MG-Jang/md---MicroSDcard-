from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
import mysql.connector
from threading import Timer
from time import sleep
import signal
import sys

def closeDB(signal, frame):
    print("BYE")
    mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    cur.close()
    db.close()
    timer.cancel()
    sys.exit(0)

def polling():
    global cur, db, ready
    
    cur.execute("select * from command order by time desc limit 1")
    for (id, time, cmd_string, arg_string, is_finish) in cur:
        if is_finish == 1 : break
        ready = (cmd_string, arg_string)
        cur.execute("update command set is_finish=1 where is_finish=0")

    db.commit()
     
    global timer
    timer = Timer(0.1, polling)
    timer.start()

def go():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.FORWARD)

def back():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.BACKWARD)

def stop():
    myMotor.setSpeed(200)
    myMotor.run(Raspi_MotorHAT.RELEASE)

def left():
    pwm.setPWM(0, 0, 357)

def mid():
    pwm.setPWM(0, 0, 407)

def right():
    pwm.setPWM(0, 0, 457)

#init
db = mysql.connector.connect(host='13.125.137.101', user='jang', password='1234', database='jangDB', auth_plugin='mysql_native_password')
cur = db.cursor()
ready = None
timer = None

mh = Raspi_MotorHAT(addr=0x6f)
myMotor = mh.getMotor(2)
pwm = PWM(0x6F)
pwm.setPWMFreq(60)

signal.signal(signal.SIGINT, closeDB)
polling()

#main thread
while True:
    sleep(0.1)
    if ready == None : continue

    cmd, arg = ready
    ready = None

    if cmd == "go" : go()
    if cmd == "back" : back()
    if cmd == "stop" : stop()
    if cmd == "left" : left()
    if cmd == "mid" : mid()
    if cmd == "right" : right()