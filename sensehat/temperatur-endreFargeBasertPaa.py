import time
from sense_hat import SenseHat

sense = SenseHat()

gronn = (0,255,0)
raud = (255,0,0)
blaa = (0,0,255)

try:
    while True:
        temperatur = sense.temp
        temperaturVerdi = temperatur / 2.5 + 16
        print(temperaturVerdi)
        if temperaturVerdi >= 28 and temperaturVerdi <= 29: # Litt spesielle krav til vanleg tmp. grunna at sensorane er kloss i CPU
            sense.clear(gronn)
        elif temperaturVerdi < 28:
            sense.clear(blaa)
        elif temperaturVerdi > 29:
            sense.clear(raud)
        else:
            sense.clear()
            print("Problem med avlesing. Temperaturverdi er problematisk.")
        time.sleep(1)
except KeyboardInterrupt:
    print("Programmet avsluttar.")
    sense.clear()