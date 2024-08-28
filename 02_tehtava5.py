
#Kysytään keskiaikaisen käyttäjän syötteet
leiviska = float(input("Anna leiviskät.\n"))
naula = float(input("\nAnna naulat.\n"))
luoti = float(input("\nAnna luodit.\n"))

#Muunnetaan keskiaikaiset mitat grammoihin
#Leiviskä = 8512g, 20 naulaa
#Naula = 425,6g, 32 luotia
#Luoti = 13,3g

#lasketaan muutos ja kg ja g
muunto = leiviska * 8512 + naula * 425.6 + luoti * 13.3
kilogram = muunto // 1000
gram = muunto % 1000

#Tulostetaan tulokset
print(f"\nMassa nykymittojen mukaan:\n"
      f"{kilogram:.0f} kilogrammaa ja {gram:.2f} grammaa.")