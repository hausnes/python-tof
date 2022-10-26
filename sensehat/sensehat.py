from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

r = 255
g = 255
b = 255

sense.clear((r,g,b))

sleep(3)

B = (102, 51, 0)
b = (0, 0, 255)
S = (205, 133, 63)
W = (255, 255, 255)

steve_pixels = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, S, S, S, S, S, S, B,
    S, S, S, S, S, S, S, S,
    S, W, b, S, S, b, W, S,
    S, S, S, B, B, S, S, S,
    S, S, B, S, S, B, S, S,
    S, S, B, B, B, B, S, S
]
steve_pixels_oye = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, S, S, S, S, S, S, B,
    S, S, S, S, S, S, S, S,
    S, S, S, S, S, b, W, S, # Lukker auge
    S, S, S, B, B, S, S, S,
    S, S, B, S, S, B, S, S,
    S, S, B, B, B, B, S, S
]

try:
    while True:
        # Her plasserer du den koden som skal køyre i "loop".
        sense.set_pixels(steve_pixels)
        sleep(random.randint(1,3))
        sense.set_pixels(steve_pixels_oye)
        sleep(0.2)
        # "Loop" ferdig
except KeyboardInterrupt:
    # Denne koden køyrer når du avsluttar programmet med CTRL+C
    sense.clear()
    print("Programmet avsluttar.")



sleep(10)

