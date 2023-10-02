# Eksempel på korleis me kan skrive data til ei CSV-fil:

verListe = [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

with open("06-verdata.csv", "w") as fil:
    fil.write("temperatur\n")
    for temperatur in verListe:
        fil.write(f"{temperatur}\n")

# Eksempel på korleis me kan lese data frå ei CSV-fil:
for linje in open("06-verdata.csv"):
    print(linje.strip()) # .strip() fjerner whitespace på slutten av linja