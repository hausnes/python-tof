import time
from sense_hat import SenseHat

sense = SenseHat()

gronn = (0,255,0)
raud = (255,0,0)
blaa = (0,0,255)

try:
    while True:
        for event in sense.stick.get_events():
            print(event.direction, event.action)
            if event.direction == "up":
                sense.clear(raud)
            elif event.direction == "down":
                sense.clear(gronn)
            elif event.direction == "left":
                sense.clear(blaa)
            elif event.direction == "right":
                sense.clear((255,255,255))
            elif event.direction == "middle":
                sense.clear()
            else:
                print("Ventar på input frå joystick..")
except KeyboardInterrupt:
    print("Programmet avsluttar.")
    sense.clear()