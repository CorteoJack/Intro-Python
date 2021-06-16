liste = [1,5,8,3,4]

plusFort = 0

for element in liste:
    if element > plusFort:
        plusFort = element

print("L'élément le plus fort est ", plusFort)
