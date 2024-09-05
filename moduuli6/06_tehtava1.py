
import random


#Aliohjelma nopanheittoa varten
def nopanheitto():
    return random.randint(1, 6)



#Pääohjelma heittää noppaa kunnes noppaluvuksi tulee 6
#samalla printataan nopan luku joka kierroksella
silmaluku = 0
while silmaluku != 6:
    silmaluku = nopanheitto()
    print(silmaluku)