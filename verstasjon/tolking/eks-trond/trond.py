import csv
from pathlib import Path

data = []

with open(Path(__file__).parent / "csvfiladi.csv", encoding="utf-8") as fil:    
    filinnholdet = csv.reader(fil, delimiter=",")
    #overskrifter = next(filinnholdet)
    for rad in filinnholdet:
        radinnhold = []        
        for verdi in rad:
            radinnhold.append(verdi)
        #print(radinnhold)
        data.append(radinnhold)

print(data[0][1])