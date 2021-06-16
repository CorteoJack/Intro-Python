import random
nombreAlea = random.randint(0,100)
print(nombreAlea)

valUsager = int(input("Entrer une valeur entre 0 et 100 : "))

while valUsager != nombreAlea:
    if valUsager == nombreAlea:
        print("Bravo!!")
    elif valUsager < nombreAlea:
        print("Trop petit")
    else:
        print("Trop grand")
    valUsager = int(input("Entrer une valeur entre 0 et 100 : "))

print("Bravo")    
