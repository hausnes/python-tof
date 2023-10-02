# import scipy
import pandas as pd

# Les inn data
# data = scipy.loadtxt('07-visualisering-data.csv', skiprows=1)
datav2 = pd.read_csv('07-visualisering-data.csv', sep=',', header=0)

# Lagre data i variablar vha pandas
tid = datav2['tidspunkt']
temperatur = datav2['temperatur']
luftfuktighet = datav2['luftfuktighet']
lufttrykk = datav2['lufttrykk']
partikkelkonsentrasjon = datav2['partikkelkonsentrasjon']

# Lagre data i variablar
# tid = data[:,0]
# temperatur = data[:,1]
# luftfuktighet = data[:,2]
# lufttrykk = data[:,3]
# partikkelkonsentrasjon = data[:,4]

# Plot temperatur
import matplotlib.pyplot as plt
plt.plot(tid, partikkelkonsentrasjon)
plt.xlabel('Tid')
plt.ylabel('PM2.5')
plt.title('Partikkelkonsentrasjon i lufta'))
# rotate labels on the x-axis
plt.xticks(rotation=90)
# save figure as png
plt.savefig('07-visualisering-plot.png')
plt.show()