import random
valgMaskin = random.choice(["stein","saks","papir"])
valgBruker = input("Skriv inn 'stein', 'saks' eller 'papir': ")
if valgMaskin == valgBruker:
    print("Uavgjort")
elif valgMaskin == "stein" and valgBruker == "saks":
    print("Datamaskin vinner")
elif valgMaskin == "papir" and valgBruker == "stein":
    print("Datamaskin vinner")
elif valgMaskin == "saks" and valgBruker == "papir":
    print("Datamaskin vinner")
else:
    print("Du vant!")

print("Maskin valgte:",valgMaskin)