# Importerer pandas for å jobbe med CSV-fila og matplotlib for å teikne grafar
import pandas as pd
import matplotlib.pyplot as plt

# Les inn data
data = pd.read_csv('07-visualisering-data.csv', sep=',', header=0)

# Lagre data i variablar vha pandas
tid = data['tidspunkt']
temperatur = data['temperatur']
luftfuktighet = data['luftfuktighet']
lufttrykk = data['lufttrykk']
partikkelkonsentrasjon = data['partikkelkonsentrasjon']

# Plot temperatur
plt.plot(tid, partikkelkonsentrasjon)
plt.xlabel('Tid')
plt.ylabel('PM2.5')
plt.title('Partikkelkonsentrasjon i lufta')
# rotate labels on the x-axis
plt.xticks(rotation=90)
# save figure as png
plt.savefig('07-visualisering-plot.png')
plt.show()