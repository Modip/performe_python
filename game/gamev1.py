import random

acteur = 50
ennemi = 50
value_potion = 3
portion = random.randint(15, 50)
attak_acteur = random.randint(5, 10)
attak_ennemi = random.randint(5, 10)

while acteur > 0 and ennemi > 0:
    print("-" * 60)
    action = int(input("Veillez choisir une action: \n 1: pour attaquer \n 2: pour une portion\n"))
    print("-" * 60)
    if action == 1:
        acteur -= attak_ennemi
        ennemi -= attak_acteur
        print("Vous avez attaquer")
        print("Il vous reste : ", acteur,"et restre ", ennemi, "à votre ennemi")
         
    elif action == 2:
        if value_potion > 0:
            value_potion -= 1
            acteur += portion
            acteur -= attak_ennemi
            print("Vous avez pris une portion, vous avez", acteur, "et il vous reste :", value_potion)
        elif value_potion <= 0 :
            print("Vous avez plus de portion, Veuillez attaquer")
    
if acteur == 0:
            print("Vous avez perdu")
else :
    print(" Bravo ! Vous avez gagner")    
           