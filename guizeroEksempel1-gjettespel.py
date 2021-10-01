from guizero import App, Text, PushButton, TextBox
import random

tilfeldigTal = random.randint(1,101)

def gjett():
    gjettaTal = int(innlestTal.value)
    if gjettaTal < tilfeldigTal:
        resultat.value = "Du gjetta for lågt."
    elif gjettaTal > tilfeldigTal:
        resultat.value = "Du gjetta for høgt."
    elif gjettaTal == tilfeldigTal:
        resultat.value = "Riktig!"
    else:
        resultat.value = "Du gjetta: " + str(gjettaTal) + ", men dette var feil."

# Set opp GUI-en (brukergrensesnittet)
app = App(title="Gjettespel")
startBeskjed = Text(app, text="Gjett på eit tal mellom 1-100!")
innlestTal = TextBox(app, width="fill")
innlestTal.focus()
button = PushButton(app, text="Gjett!", command=gjett)
resultat = Text(app, text="")

app.display()