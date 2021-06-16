import tkinter as tk
root = tk.Tk()
label = tk.Label(root, text="Devine le nombre!", fg ='red')

label.pack()


value = StringVar()
value.set("Texte par défaut")
fenetre=()
entree = Entry(fenetre, textvariable=int, width=30)
entree.pack()
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "Entrer une valeur entre 0 et 100: ")
btn = Button(root, text='Fermer', command=root.quit)
btn.pack()



fen.mainloop()
