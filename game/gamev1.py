import random

acteur = 50
ennemi = 50
portion = random.randint(15, 50)
attak_acteur = random.randint(5, 10)
attak_ennemi = random.randint(5, 10)

while acteur > 0 and ennemi > 0:
    action = int(input("Veillez choisir une action: \n 1: pour attaquer \n 2: pour une portion\n"))
    if action == 1:
        acteur -= attak_ennemi
        ennemi -= attak_acteur
        print("Vous avez attaquer")
        print("Il vous reste : ", acteur)
    if acteur == 0:
        print("Vous avez perdu")
        break
    elif action == 2:
        acteur += portion
        print("Vous avez pris une portion, vous avez", acteur)
    else:
        print("Veillez choisir entre 1 et 2")