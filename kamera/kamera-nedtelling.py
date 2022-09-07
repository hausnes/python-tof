from sense_hat import SenseHat
import time
from picamera import PiCamera

s = SenseHat()
kam = PiCamera()
kam.resolution = (640,480)

tidForFoto = 5

g = (255, 255, 0)
b = (0, 0, 0)

smil = [
    g, g, g, g, g, g, g, g,
    g, g, b, g, g, b, g, g,
    g, g, g, g, g, g, g, g,
    b, g, g, g, g, g, g, b,
    g, b, g, g, g, g, b, g,
    g, g, b, b, b, b, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g
]

kam.start_preview(alpha=200)

for x in range(tidForFoto,0,-1):
    print(x)
    s.show_letter(str(x))
    time.sleep(1)

s.set_pixels(smil)
kam.capture('/home/pi/Desktop/foto.jpg')
kam.stop_preview()
time.sleep(3)
s.clear()