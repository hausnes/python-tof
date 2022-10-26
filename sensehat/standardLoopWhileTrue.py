'''
Standardmal for korleis de kan ha ein "evig" loop gåande
heilt til brukaren avsluttar programmet ved å trykke på
CTRL+c
'''

import time
import sys

try:
    while True:
        # Her plasserer du den koden som skal køyre i "loop".
        print("Programmet køyrer.")
        time.sleep(1)
        # "Loop" ferdig
except KeyboardInterrupt:
    # Denne koden køyrer når du avsluttar programmet med CTRL+C
    print("Programmet avsluttar.")
    sys.exit()