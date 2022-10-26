from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

# Innstillingar
plasseringX = 0 # Startplassering for pikselen (NB: 0,0 oppe i venstre hjørne. Pos. x til høgre, pos. y nedover)
plasseringY = 0
fargePiksel = (0, 0, 255)
fart = 0.01 # Eigentleg, "sovetid" mellom kvar pixel-påslåing. Lågare tal, raskare oppdatering
antallIterasjonar = 1
fjernGamlePiksler = True # Skal pikslane bli ståande på eller bli slått av for kvar nye oppteikning?

# Ein funksjon me kan bruke om me vil, for å teikne med tilfeldig farge
def tilfeldigFarge():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  return (r, g, b)

for x in range(antallIterasjonar):
  sense.clear()
  
  # Ein loop som set fargar på alle pikslane ein og ein
  for x in range(0,8): # NB: 0 til og med 7, gjer 8 ulike verdiar
    for y in range (0,8):
      sense.set_pixel(plasseringX+x, plasseringY+y, tilfeldigFarge()) # Byt gjerne ut "tilfeldigFarge()" med "fargePiksel" om du vil ha same farge
      sleep(fart)
      if fjernGamlePiksler:
        sense.clear()
  
  sense.clear()
  
  for y in range(0,8): # NB: 0 til og med 7, gjer 8 ulike verdiar
    for x in range (0,8):
      sense.set_pixel(plasseringX+x, plasseringY+y, fargePiksel)
      sleep(fart)
      if fjernGamlePiksler:
        sense.clear()
      
sense.clear() # Slår av alt tilslutt