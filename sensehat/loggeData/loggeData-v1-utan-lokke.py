'''
Dette programmet er meint å køyre vha. crontab ved faste intervall.
Det er grunna dette inga uendeleg løkke.
I tillegg blir det i linje 60 brukt 'a' for å appende/legge til på
slutten av csv-fila kvar gong programmet køyres. Merk at det pga.
dette er laga ei csv-fil med header i forkant.
'''

from sense_hat import SenseHat
from datetime import datetime
from csv import writer

sense = SenseHat()

def get_sense_data():
    sense_data = []
    # Get environmental data
    sense_data.append(sense.get_temperature())
    sense_data.append(sense.get_pressure())
    sense_data.append(sense.get_humidity())
    
    '''
    # Get colour sensor data (version 2 Sense HAT only)
    red, green, blue, clear = sense.colour.colour
    sense_data.append(red)
    sense_data.append(green)
    sense_data.append(blue)
    sense_data.append(clear)
    
    # Get orientation data
    orientation = sense.get_orientation()
    sense_data.append(orientation["yaw"])
    sense_data.append(orientation["pitch"])
    sense_data.append(orientation["roll"])
    
    # Get compass data
    mag = sense.get_compass_raw()
    sense_data.append(mag["x"])
    sense_data.append(mag["y"])
    sense_data.append(mag["z"])
    
    # Get accelerometer data
    acc = sense.get_accelerometer_raw()
    sense_data.append(acc["x"])
    sense_data.append(acc["y"])
    sense_data.append(acc["z"])
    
    # Get gyroscope data
    gyro = sense.get_gyroscope_raw()
    sense_data.append(gyro["x"])
    sense_data.append(gyro["y"])
    sense_data.append(gyro["z"])
    '''

    # Get the date and time
    sense_data.append(datetime.now())

    return sense_data

with open('loggeData-v1.csv', 'a', newline='') as f: # NB: 'a' legg til, og derfor har me lagt til header i dataCrontab.csv i forkant
    data_writer = writer(f)
    data = get_sense_data()
    data_writer.writerow(data)