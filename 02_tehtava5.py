
#Kysytään keskiaikaisen käyttäjän syötteet
leiviska = float(input("Anna leiviskät.\n"))
naula = float(input("\nAnna naulat.\n"))
luoti = float(input("\nAnna luodit.\n"))

#Muunnetaan keskiaikaiset mitat grammoihin
#Leiviskä = 8512g, 20 naulaa
#Naula = 425,6g, 32 luotia
#Luoti = 13,3g

#lasketaan muutos, erilaisia tapoja.

#Voidaan muuttaa leiviskat -> nauloihin -> luoteihin
#Ja lopulta muutetaan grammoiksi
#naula = leiviska * 20 + naula
#luoti = naula * 32 + luoti
#gram = luoti * 13.3

#Tai lasketaan suoraan, omasta mielestä simppelimpi
gram = leiviska * 20*32*13.3 + naula * 32 * 13.3 + luoti * 13.3
#gram = leiviska * 8512 + naula * 425.6 + luoti * 13.3

kilogram = gram // 1000
gram = gram % 1000

#Tulostetaan tulokset
print(f"\nMassa nykymittojen mukaan:\n"
      f"{kilogram:.0f} kilogrammaa ja {gram:.2f} grammaa.")