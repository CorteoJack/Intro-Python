import tkinter as tk
import random


def go():
    valInt = int(valEntree.get())
    if valInt == nombreAleatoire:
        labelValid.config(text="BRAVO!!!", fg="green")

    elif valInt < nombreAleatoire:
        labelValid.config(text="Trop Bas!!!", fg="red")
    else:
        labelValid.config(text="Trop Haut!!!", fg="red")


nombreAleatoire = random.randint(0, 100)

root = tk.Tk()
label = tk.Label(root, text="Devine le nombre!", fg="red")
label.pack()
labelInst = tk.Label(root, text="Entrer une valeur entre 0 et 100", fg="black")
labelInst.pack()
labelValid = tk.Label(root, text="")
labelValid.pack()
value = tk.StringVar()
value.set("Texte par défaut")
fenetre = ()
valEntree = tk.StringVar()
entree = tk.Entry(fenetre, textvariable=valEntree, width=30)
entree.pack()
btnFermer = tk.Button(root, text="Fermer", command=root.quit)
btnFermer.pack()
btnGo = tk.Button(root, text="Go", command=go)
btnGo.pack()


root.mainloop()
