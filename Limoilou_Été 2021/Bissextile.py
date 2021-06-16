annee = input ("Entrer une année : ")
annee = int(annee)

bissextile = False

if annee % 4 != 0:
    bissextile = False
elif annee % 4 ==0:
    if annee %100 != 0:
        bissextile = True
    elif annee %100 ==0:
        if annee %400 != 0:
            bissextile = False
        else:
            bissextile = True


if bissextile :
    print("L'année entrée est bissextile")
else:
    print("L'année entrée n'est pas bissextile")
    
