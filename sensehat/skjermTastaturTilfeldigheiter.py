from sense_hat import SenseHat
from time import sleep
import random
import sys

sense = SenseHat()

# Innstillingar
sovetider = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7] # Ei liste med tider i intervall på 0.1 (mellom 0 og 1)
antallIterasjonar = 30
#type = "enkeltPiksler"
#type = "heileSkjermen"
kjorer = "jepp" # Blbalba

# Ein funksjon me kan bruke om me vil, for å teikne med tilfeldig farge
def tilfeldigFarge():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  return (r, g, b)

# Her skjer sjølve oppdateringa av skjermen, basert på innstillingane øverst
def koyrerSkjermOppdatering(innType):
  #global sovetider
  print("Sovetider:",sovetider)
  
  for x in range(0,antallIterasjonar): # dersom "antallIterasjonar" er lik 1 så køyrer dette berre ein gong
    sense.clear()
    
    type = innType
    
    # Enkeltpikslar
    if type == "enkeltPiksler":
      plasseringX = random.randint(0,7)
      plasseringY = random.randint(0,7)
      fart = sovetider[random.randint(0,len(sovetider)-1)]
      print(fart)
      sense.set_pixel(plasseringX, plasseringY, tilfeldigFarge())
      sleep(sovetider[random.randint(0,len(sovetider)-1)])
    
    # Heile skjermen
    if type == "heileSkjermen":
      fart = sovetider[random.randint(0,len(sovetider)-1)]
      print(fart)
      sense.clear(tilfeldigFarge())
      sleep(fart)
  
  # Avsluttar programmet
  sense.clear() # Nullstiller skjermen tilslutt

# Hovedloopen, som køyrer heilt til du trykker inn joysticka. Opp er enkeltpiksler, ned er 
while kjorer == "jepp":
  for event in sense.stick.get_events():
      #print(event.direction, event.action)
      if event.direction == "up" and event.action == "pressed":
          koyrerSkjermOppdatering("enkeltPiksler")
      elif event.direction == "down" and event.action == "pressed":
          koyrerSkjermOppdatering("heileSkjermen")
      elif event.direction == "middle" and event.action == "pressed":
          sys.exit()
      else:
          print("Ventar på input frå joystick..")