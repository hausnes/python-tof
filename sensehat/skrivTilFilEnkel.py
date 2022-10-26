# Enkelt eksempel på korleis du kan skrive til og lese frå fil:
# https://www.w3schools.com/python/python_file_write.asp
# 'a' betyr append, altså å legge til. '\n' betyr linjeskift

f = open("data.txt", "a")
dataEks = 4555.6
f.write(str(dataEks)+"\n")
f.write("Now the file has more content!\n")
f.close()

# Etter at me har lagt til data i fila over, så opnar me den,
# les alt innhaldet (r) og skriv det ut:
f = open("data.txt", "r")
print(f.read())