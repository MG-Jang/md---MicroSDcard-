from sense_hat import SenseHat
import time

sense = SenseHat()
#sense.show_message("jang Myoung geun")


X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

map = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
    ]

sense.set_pixels(map)