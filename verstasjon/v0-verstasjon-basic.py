#!/usr/bin/env python3

'''
Forklaring:
Køyrer ein uendeleg loop som loggar data kvar X-te sekund (skift var. delay til ønska verdi)

Anbefalt å køyre vha. crontab som fylgjer:
@reboot sleep 240 && sudo python3 /home/pi/v0-verstasjon-basic.py 

NB: Lag ei csv-fil med overskrift-rad om du ynskjer det. Legg merke til 
at det ved skriving til csv-fil blir lagt til ny linje (a for append).
'''

import requests
import ST7735
import time
from datetime import datetime
from csv import writer
from bme280 import BME280
from pms5003 import PMS5003, ReadTimeoutError, ChecksumMismatchError
from subprocess import PIPE, Popen, check_output
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium as UserFont

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
import logging

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logging.info("""Verstasjon - Reads temperature, pressure, humidity,
#PM2.5, and PM10 from Enviro plus and sends data to CSV
#and Thingspeak.

#Press Ctrl+C to exit!

#""")

bus = SMBus(1)

# Create BME280 instance
bme280 = BME280(i2c_dev=bus)

# Create LCD instance
disp = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)

# Initialize display
disp.begin()

# Create PMS5003 instance
pms5003 = PMS5003()

timestamp = datetime.now()
delay = 5

def hentData():
    values = []

    values.append(datetime.now())
    
    cpu_temp = get_cpu_temperature()
    raw_temp = bme280.get_temperature()
    comp_temp = raw_temp - ((cpu_temp - raw_temp) / comp_factor)
    values.append(comp_temp)

    trykk = bme280.get_pressure() * 100
    values.append(trykk)

    fukt = bme280.get_humidity()
    values.append(fukt)

    try:
        pm_values = pms5003.read()
        values.append(str(pm_values.pm_ug_per_m3(2.5)))
        values.append(str(pm_values.pm_ug_per_m3(10)))
    except(ReadTimeoutError, ChecksumMismatchError):
        logging.info("Failed to read PMS5003. Reseting and retrying.")
        pms5003.reset()
        pm_values = pms5003.read()
        values.append(str(pm_values.pm_ug_per_m3(2.5)))
        values.append(str(pm_values.pm_ug_per_m3(10)))
    
    return values

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp

# Get Raspberry Pi serial number to use as ID
def get_serial_number():
    with open('/proc/cpuinfo', 'r') as f:
        for line in f:
            if line[0:6] == 'Serial':
                return line.split(":")[1].strip()

# Check for Wi-Fi connection
def check_wifi():
    if check_output(['hostname', '-I']):
        return True
    else:
        return False

# Display Raspberry Pi serial and Wi-Fi status on LCD
def display_status():
    wifi_status = "connected" if check_wifi() else "disconnected"
    text_colour = (255, 255, 255)
    back_colour = (0, 170, 170) if check_wifi() else (85, 15, 15)
    id = get_serial_number()
    message = "{}\nWi-Fi: {}".format(id, wifi_status)
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    size_x, size_y = draw.textsize(message, font)
    x = (WIDTH - size_x) / 2
    y = (HEIGHT / 2) - (size_y / 2)
    draw.rectangle((0, 0, 160, 80), back_colour)
    draw.text((x, y), message, font=font, fill=text_colour)
    disp.display(img)

# Compensation factor for temperature
comp_factor = 2.25

# Raspberry Pi ID to send to Luftdaten
id = "raspi-" + get_serial_number()

# Width and height to calculate text position
WIDTH = disp.width
HEIGHT = disp.height

# Text settings
font_size = 16
font = ImageFont.truetype(UserFont, font_size)

# Log Raspberry Pi serial and Wi-Fi status
logging.info("Raspberry Pi serial: {}".format(get_serial_number()))
logging.info("Wi-Fi: {}\n".format("connected" if check_wifi() else "disconnected"))

with open('verstasjon-v0.csv', 'a', newline='') as f: # NB: 'w' betyr at alt som låg i fila frå før blir overskrive. 'a' legg til, men pass på å då fjerne overskriftene
    data_writer = writer(f)
    #data_writer.writerow(['tidspunkt','temperatur', 'trykk', 'fuktighet','pm25','pm10']) # NB: Legg til dei andre sensoroverskriftene om du bruker dei
    while True:
        data = hentData()
        time_difference = data[0] - timestamp
        if time_difference.seconds > delay:
            logging.info(data)
            data_writer.writerow(data)
            timestamp = datetime.now()
        display_status()