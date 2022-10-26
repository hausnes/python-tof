from sense_hat import SenseHat
from time import sleep
from datetime import datetime
from csv import writer
import csv

sense = SenseHat()

tidsstempel = datetime.now()
forsinkelse = 5

def hentData():
    listeVerdata = []

    pressure = sense.get_pressure()
    #print("Trykk:",round(pressure,2))
    listeVerdata.append(pressure)
    
    temp = sense.get_temperature()
    #print("Temperatur:",round(temp,2))
    listeVerdata.append(temp)
    
    humidity = sense.get_humidity()
    #print("Fuktighet:",round(humidity,2))
    listeVerdata.append(humidity)

    # Legg til tidsstempel òg
    listeVerdata.append(datetime.now())
    
    return listeVerdata

# Maaling, basert paa https://projects.raspberrypi.org/en/projects/sense-hat-data-logger
with open('verdata.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    while True:
        data = hentData()
        dt = data[-1] - tidsstempel
        #print(dt.seconds)
        if dt.seconds > forsinkelse:      
            print("Full liste denne runden:",data)
            writer.writerow(data)
            tidsstempel = datetime.now()