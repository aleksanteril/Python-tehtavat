import random

#Kysytään käyttäjältä syöte
#arpakuutioiden määrästä
noppalkm = int(input("Kuinka monta noppaa heitetään? "))
silmaluvut = []

#Heitetään for loopilla
#Se määrä random.randomint kuin "Noppia"
for i in range(noppalkm):
    silmaluvut.append(random.randint(1, 6))

#Lasketaan for loopilla yhteen lista
summa = 0
for num in silmaluvut:
    summa += num

#Tulostetaan saatu summa
print(summa)

