
import random


#Aliohjelma nopanheittoa varten, parametri tahkojen lukumäärä
def nopanheitto(tahkolkm):
    return random.randint(1, tahkolkm)



#Pääohjelma heittää noppaa kunnes noppaluvuksi tulee isoin mahdollinen
#samalla printataan nopan luku joka kierroksella
tahkolkm = int(input("Anna tahkojen lukumäärä: "))
silmaluku = 0
while silmaluku != tahkolkm:
    silmaluku = nopanheitto(tahkolkm)
    print(silmaluku)