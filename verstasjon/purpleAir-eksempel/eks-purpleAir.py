from purpleair import PurpleAir

# Create a PurpleAir object with your API key
pa = PurpleAir("3C2A27E8-4CA8-11EE-A77F-42010A800009")

print(pa.check_key("3C2A27E8-4CA8-11EE-A77F-42010A800009"))
tempEksempel = pa.get_sensor_data("174371",fields=("temperature","pm2.5"))
print(tempEksempel)
print(tempEksempel['sensor']["temperature"])

# Konverter  tempEksempel frå fahrenheit til celsius
tempC = (tempEksempel['sensor']["temperature"] - 32) * 5.0/9.0

print("Temperaturen per no:",tempC)

print(tempEksempel['sensor']["pm2.5"])