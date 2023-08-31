from sense_hat import SenseHat
from time import sleep

sense =SenseHat()

while True:
    ori = sense.get_orientation_degrees()
    print(f'[{ori["pitch"]: 5.1f}] - ', end = '')
    print(f'[{ori["roll"]: 5.1f}] - ', end = '')
    print(f'[{ori["yaw"]: 5.1f}]', end = '')
    print()