import random

#Kysytään käyttäjältä syöte
#arpakuutioiden määrästä
noppalkm = int(input("Kuinka monta noppaa heitetään? "))
silmaluvut = []

#Heitetään for loopilla
#Se määrä random.randomint kuin "Noppia"
for i in range(noppalkm):
    silmaluvut.append(random.randint(1, 6))

#Tulostetaan noppien lukujen summa
#print(silmaluvut)
print (sum(silmaluvut))

