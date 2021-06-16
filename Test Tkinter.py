from tkinter import*
fen = Tk()
label = Label(fen,text="Allo!", fg='red')
btn = Button(fen, text='Fermer', command=fen.quit)

label.pack()
btn.pack()

fen.mainloop()
