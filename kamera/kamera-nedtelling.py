from sense_hat import SenseHat
from picamera2 import Picamera2, Preview
import time
from datetime import datetime

s = SenseHat()
kam = Picamera2()
kamConfig = kam.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
kam.configure(kamConfig)

tidForFoto = 5 # 5 sekund før biletet blir tatt

g = (255, 255, 0) # gul
b = (0, 0, 0)

smil = [ # smiley
    g, g, g, g, g, g, g, g,
    g, g, b, g, g, b, g, g,
    g, g, g, g, g, g, g, g,
    b, g, g, g, g, g, g, b,
    g, b, g, g, g, g, b, g,
    g, g, b, b, b, b, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g
]

kam.start_preview(Preview.QTGL) 
kam.start()

for x in range(tidForFoto,0,-1):
    print(x)
    s.show_letter(str(x))
    time.sleep(1)

s.set_pixels(smil)

filnavn = str(datetime.now()) + ".jpg"

time.sleep(2)
kam.capture_file("/home/pi/Pictures/" + filnavn) # Endre til riktig sti (og filnavn) for ditt prosjekt

time.sleep(2)
s.clear()