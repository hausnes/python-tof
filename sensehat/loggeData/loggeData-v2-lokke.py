'''
Dette programmet er meint å logge data "uendeleg", med ein viss 'delay' ml. kvar måling.
Dersom du ynskjer å køyre programmet vha. crontab så anbefalast det derfor å starte det 
ved reboot (ikkje faste intervall), samt å vere bevisst på at 'w' i linje 63 gjer at alle
data som var i csv-fila frå før blir overskrive. 'a' legg til, men ver då bevisst på at
header blir lagt til for kvar gong (sjå løysning på dette i v1-utan-lokke).
'''

from sense_hat import SenseHat
from datetime import datetime
from csv import writer

sense = SenseHat()

timestamp = datetime.now()
delay = 1

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

with open('loggeData-v2.csv', 'w', newline='') as f: # NB: 'w' betyr at alt som låg i fila frå før blir overskrive. 'a' legg til, men pass på å då fjerne overskriftene
    data_writer = writer(f)
    data_writer.writerow(['temperatur', 'trykk', 'fuktighet','datetime']) # NB: Legg til dei andre sensoroverskriftene om du bruker dei
    while True:
        data = get_sense_data()
        time_difference = data[-1] - timestamp
        if time_difference.seconds > delay:
            data_writer.writerow(data)
            timestamp = datetime.now()