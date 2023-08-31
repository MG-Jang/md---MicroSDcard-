# Ic2 센서

> BMP280의 주소값 확인(이 주소값을 DEVICE_ADDR 에 넣어야함)
- $ i2cdetect -y 1

> 레지스터에 정상 연결되었는지 확인 0이 출력되면 됨.
```py
import smbus
from time import sleep
DEVICE_BUS = 1
DEVICE_ADDR = 0x76
bus = smbus.SMBus(DEVICE_BUS)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)

while True:
    a = bus.read_
```