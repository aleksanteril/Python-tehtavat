
import random

#Kone arpoo luvun 1-10 muistiin
rand_luku = random.randint(1,10)
player_guess = None

#Kysytään pelaajalta lukua ja verrataan arvottuun lukuun antaen vihjeitä
while(player_guess != rand_luku):
    player_guess = int(input("Arvaa luku välillä 1 - 10: "))
    if player_guess < rand_luku:
        print("Liian pieni arvaus")
    elif player_guess > rand_luku:
        print("Liian suuri arvaus")

#Jos luku on sama kuin arvottu luku poistutaan loopista ja printataan onnittelut
print("\nOkein")
