
#Funktio saa parametrina listan
#Funktio karsii listasta parittomat luvut pois
#Funktio palauttaa listan

def pariton_karsinta(listaint):
    pari_listaint =[]
    for num in listaint:
        if num % 2 == 0:
            pari_listaint.append(num)
    return pari_listaint


#Pääohjelma testausta varten
listaint = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pari_listaint = pariton_karsinta(listaint)
print(listaint)
print(pari_listaint)
