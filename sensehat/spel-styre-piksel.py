import time
from sense_hat import SenseHat

sense = SenseHat()

plasseringX = 0 # Startplassering for pikselen (NB: 0,0 oppe i venstre hjørne. Pos. x til høgre, pos. y nedover)
plasseringY = 0
fargePiksel = (0, 0, 255)
fargeAlarmPiksel = (255, 0, 0)
kjorer = "jepp"

def blinkAlarmTraffVeggen(xInn, yInn):
  sense.set_pixel(xInn, yInn,fargeAlarmPiksel)
  time.sleep(0.2)
  sense.set_pixel(xInn, yInn,fargePiksel)
  time.sleep(0.2)
  sense.set_pixel(xInn, yInn,fargeAlarmPiksel)
  time.sleep(0.2)
  sense.set_pixel(xInn, yInn,fargePiksel)
  time.sleep(0.2)

def flytt(inndata):
  global plasseringX
  global plasseringY
  
  if inndata == "opp":
    if plasseringY-1 >= 0:
      plasseringY -= 1
      print("Opp","plasseringX =",plasseringX,"plasseringY =",plasseringY)
    else:
      print("Opp, men nådd toppen","plasseringX =",plasseringX,"plasseringY =",plasseringY)
      blinkAlarmTraffVeggen(plasseringX,plasseringY)
    sense.clear()
    sense.set_pixel(plasseringX,plasseringY,fargePiksel)
  
  if inndata == "ned":
    if plasseringY+1 <= 7:
      plasseringY += 1
      print("Ned","plasseringX =",plasseringX,"plasseringY =",plasseringY)
    else:
      print("Ned, men nådd bunnen","plasseringX =",plasseringX,"plasseringY =",plasseringY)
      blinkAlarmTraffVeggen(plasseringX,plasseringY)
    sense.clear()
    sense.set_pixel(plasseringX,plasseringY,fargePiksel)
  
  if inndata == "venstre":
    if plasseringX-1 >= 0:
      plasseringX -= 1
      print("Venstre","plasseringX =",plasseringX,"plasseringY =",plasseringY)
    else:
      print("Venstre, men naadd veggen","plasseringX =",plasseringX,"plasseringY =",plasseringY)
      blinkAlarmTraffVeggen(plasseringX,plasseringY)
    sense.clear()
    sense.set_pixel(plasseringX,plasseringY,fargePiksel)
  
  if inndata == "hogre":
    if plasseringX+1 <= 7:
      plasseringX += 1
      print("Hogre","plasseringX =",plasseringX,"plasseringY =",plasseringY)
    else:
      print("Hogre, men naadd veggen","plasseringX =",plasseringX,"plasseringY =",plasseringY)
      blinkAlarmTraffVeggen(plasseringX,plasseringY)
    sense.clear()
    sense.set_pixel(plasseringX,plasseringY,fargePiksel)

while kjorer == "jepp":
  for event in sense.stick.get_events():
      #print(event.direction, event.action)
      if event.direction == "up" and event.action == "pressed":
          flytt("opp")
      elif event.direction == "down" and event.action == "pressed":
          flytt("ned")
      elif event.direction == "left" and event.action == "pressed":
          flytt("venstre")
      elif event.direction == "right" and event.action == "pressed":
          flytt("hogre")
      elif event.direction == "middle" and event.action == "pressed":
          flytt("klikk")
      else:
          print("Ventar på input frå joystick..")
