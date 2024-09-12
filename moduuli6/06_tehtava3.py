
#Funktio jossa muutetaan US gallona ja palautetaan
#Modernin maailman litra

#Yksi gallona on 3,785 litraa
def gal_to_lit(gallon):
    return gallon*3.785

#Kysytään käyttäjältä syöte kunnes käyttäjä syöttää negatiivisen luvun
gal = float(input("Syötä gallona määrä, jos haluat lopettaa syötä tyhjä: "))
while gal >= 0:
    litra = gal_to_lit(gal)
    print(litra)
    gal = float(input("Syötä gallona määrä, jos haluat lopettaa syötä tyhjä: "))