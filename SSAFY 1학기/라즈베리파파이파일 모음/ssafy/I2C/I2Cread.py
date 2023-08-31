import smbus
from bmp280 import BMP280
from time import sleep
DEVICE_BUS = 1
DEVICE_ADDR = 0x76
bus = smbus.SMBus(DEVICE_BUS)
#bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)

while True:
    a = bus.read_byte_data(DEVICE_ADDR, 0xFB)
    b = bus.read_byte_data(DEVICE_ADDR, 0xFA)
    c = bus.read_byte_data(DEVICE_ADDR, 0xFC)
    
    print(a, b, c)
    result = (a << 12) | (b<<4) | ((c& 0xF0) >> 4)
    
    print(result)
    sleep(0.5)