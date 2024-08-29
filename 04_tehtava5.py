
#Luodaan vakioarvot ja muuttujat, yritysten määrä muuttuja helppoa testiä varten
user = "python"
passw = "rules"
tries_amount = 5
tries = inp_user = inp_passw = 0

#While kysyy käyttäjältä inputtia kunnes käyttis ja salis on match tai
#Yritysten määrä on ylittänyt asetetun arvon 5
while (inp_user != user or inp_passw != passw) and tries != tries_amount:
    inp_user = input("\nSyötä käyttäjätunnus: ")
    inp_passw = input("Syötä salasana: ")
    tries = tries + 1

#Printataan tulos käyttäjälle, jos yritykset ylittyivät niin pääsy evätty
#Muuten ok tervetuloa
if tries == tries_amount:
    print("\nPääsy evätty")
else:
    print("\nTervetuloa!")



