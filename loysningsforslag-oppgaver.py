# 1.2
tallEin = 5
tallTo = 10
resultat = tallEin * tallTo
print(tallEin,"ganger",tallTo,"er",resultat)

# 1.2: Meir avansert løysing
tallInnlest1 = int(input("Tall 1: "))
tallInnlest2 = int(input("Tall 2: "))
resultat = tallInnlest1 * tallInnlest2
print(tallInnlest1,"ganger",tallInnlest2,"er",resultat)

# 1.3: Be gjerne om input frå brukaren, slik at det blir generert ei e-postadresse
fornavn = "jo"
mellomnavn = "bjornar"
etternavn = "hausnes"
domene = "gmail.com"
epost = fornavn + "." + mellomnavn + "." + etternavn + "@" + domene
print(epost)

# 1.3: Alternativ 2, variant
navn = "Jo Bjornar"
print(navn.lower()) # Denne gjer alt i 'navn' om til små bokstavar
print(navn.lower().replace(" ","")) # Denne fjernar mellomrom i navn, i tillegg til å gjere om til små bokstavar

# 1.5
gate = "Kongens Gate"
husnr = 432
oppgang = "b"
adresse = gate + " " + str(husnr) + oppgang
print(adresse)
print("Adressen er",gate,husnr,oppgang)
print("Gaten er " + gate + ", husnummeret er " + str(husnr) + ", oppgang " + oppgang + ".")

# 1.6
prisMatDrikke = 850
studentRabatt = 0.25
tips = 0.10
sumMiddag = prisMatDrikke + (prisMatDrikke * tips) - (prisMatDrikke * studentRabatt)
print("Middagen, inkl. drikke, kostar:",sumMiddag,"kroner.")

antPersoner = int(input("Kor mange personar skal dele på rekninga? "))
prisPerPerson = sumMiddag / antPersoner
print("Kvar person i ditt følge på",antPersoner,"personar, skal betale:",round(prisPerPerson,2),"kroner.")