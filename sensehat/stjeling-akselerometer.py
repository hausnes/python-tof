import time
from sense_hat import SenseHat

sense = SenseHat()

gronn = (0,255,0)
raud = (255,0,0)
blaa = (0,0,255)

try:
    while True:
        x,y,z = sense.get_accelerometer_raw().values()
        x = abs(x)
        y = abs(y)
        z = abs(z)
        
        if x > 1 or y > 1 or z > 1:
            sense.clear(raud)
            time.sleep(1)
        else:
            #print("Ingenting skjer..")
            sense.clear(gronn)

except KeyboardInterrupt:
    print("Programmet avsluttar.")
    sense.clear()