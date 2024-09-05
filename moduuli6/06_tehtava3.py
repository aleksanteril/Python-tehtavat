
#Funktio jossa muutetaan US gallona ja palautetaan
#Modernin maailman litra

#Yksi gallona on 3,785 litraa
def gal_to_lit(gallon):
    return gallon*3.785

#Kysytään käyttäjältä syöte kunnes käyttäjä syöttää tyhjän
galstr = input("Syötä gallona määrä, jos haluat lopettaa syötä tyhjä: ")
while galstr != "":
    litra = gal_to_lit(float(galstr))
    print(litra)
    galstr = input("Syötä gallona määrä, jos haluat lopettaa syötä tyhjä: ")