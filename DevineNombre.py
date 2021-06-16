import random

nombreAleatoire = random.randint(0,100)

gagne = False

while gagne == False:
    valUsager = input("Entrer une valeur entre 0 et 100: ")
    valUsager = int(valUsager)
    if valUsager == nombreAleatoire:
        gagne = True
        print("Bravo!")

    elif valUsager<nombreAleatoire:
        print("Tros bas!")
    else:
        print("Trop haut!")


