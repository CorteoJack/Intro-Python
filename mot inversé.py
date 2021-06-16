while True:
    motUsager = input("Tapez une chaine de caractères : ")
    
    motInv = ""
    for lettre in motUsager:
         motInv = lettre + motInv
    print('le mot inversé est ', motInv)



