
#Kysytään kalastajan kuhan mitta
#Ja tehdään vakiomuuttuja laskuja varten CM
kuha_mitta = float(input("Syötä kuhan mitta senttimetreinä: "))
kuha_alamitta = 37


#Jos alamittainen käskee laskemaan takaisin järveen
#Laskee samalla monta cm puuttuu mitasta
if kuha_mitta < kuha_alamitta:
    print(f"\nLaske kuha takaisin järveen!\n"
          f"Kuha on {(kuha_alamitta - kuha_mitta):.1f}cm alle sallitun mitan!")


#Kuha on alamittainen jos sen pituus on <37cm
