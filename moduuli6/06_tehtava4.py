
#Aliohjelma joka summaa listan yhteen
def lista_summaus(numlista):
    return sum(numlista)


#Pääohjelma jossa kutsutaan aliohjelmaa ja tulostetaan tulos
intlista = [1, 6 , 7 , 24, 13]
intlista_tulos = lista_summaus(intlista)
print (intlista_tulos)