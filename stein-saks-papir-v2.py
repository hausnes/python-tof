import random

antVinnSpelar = 0
antallRundar = 0
fleireRundar = "j"

while fleireRundar == "j":
    antallRundar += 1
    valgMaskin = random.choice(["stein","saks","papir"])
    valgBruker = input("\nSkriv inn 'stein', 'saks' eller 'papir': ")
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
        antVinnSpelar += 1
        
    print("Maskin valgte: ",valgMaskin)

    print("\nLyst til å spele ein runde til? (j/n):")
    fleireRundar = input("").lower()

# Spelet er ferdig. Oppsummerer:
print("\nSpelaren vant",antVinnSpelar,"av",antallRundar)