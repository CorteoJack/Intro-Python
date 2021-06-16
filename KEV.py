import tkinter as tk
from tkinter.filedialog import *

filepath = askopenfilename(
    title="Ouvrir une image", filetypes=[("png files", ".png"), ("all files", ".*")]
)
fenetre = Tk()
photo = PhotoImage(file=filepath)
canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="yellow")
canvas.create_image(50, 50, anchor=NW, image=photo)
canvas.pack()
