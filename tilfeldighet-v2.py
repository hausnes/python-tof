import random

for x in range(0,11): # (0,11,1) 
    print("Runde",x,":")
    print(random.choice(["stein","saks","papir"]))
    print(random.randint(1,10))
    
lestInnVerdi = int(input("Kva tal skal eg telle ned frå? "))

while lestInnVerdi >= 0:
    print(lestInnVerdi)
    lestInnVerdi -= 1 # NB: Forsøk gjerne å fjerne denne. Kva skjer?
