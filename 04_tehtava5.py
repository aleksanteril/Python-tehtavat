
user = "python"
passw = "rules"
tries = 0


while(tries != 5):
    inp_user = input("Syötä käyttäjätunnus: ")
    inp_passw = input("Syötä salasana: ")
    if inp_user != user or inp_passw != passw:
        print("\nPääsy evätty")
        tries = tries + 1
    elif inp_user == user and inp_passw == passw:
        print("\nTervetuloa")
        break



