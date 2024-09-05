
#Aliohjelma joka summaa listan yhteen

#Myös voisi käyttää sum funktiota!!
#Aliohjelma listan summaukseen
def summaus(numlista):
    sum = 0
    for num in numlista:
        sum += num
    return sum

#Pääohjelma jossa kutsutaan aliohjelmaa ja tulostetaan tulos
intlista = [1, 8, 6, 5]
intlista_tulos = summaus(intlista)
print (intlista_tulos)