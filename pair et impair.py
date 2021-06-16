liste = [1,2,3,4,5,6,7,8,9]

pair = []
impair = []

for element in liste:
    if element%2 == 0:
        pair.append(element)
    else:
        impair.append(element)

print("Les valeurs pairs sont : ", pair)
print("Les valeurs impairs sont : ", impair)
