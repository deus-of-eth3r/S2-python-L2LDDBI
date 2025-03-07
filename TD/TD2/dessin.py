import tkinter as tk
from random import randint


fenetre = tk.Tk()
fenetre.title = "DESSINE"
#Changement de couleur
boutoncoul=tk.Button(fenetre,text="Choisir couleur mon copain",command=lambda:couleurfct())
boutoncoul.grid(row = 1,column=1)

boutondisque=tk.Button(fenetre,text="Un cercle",command=lambda :disque())
boutondisque.grid(row=1,column=0)

boutonrect=tk.Button(fenetre,text="Un rectangle",command=lambda :rectangle())
boutonrect.grid(row=2,column=0)

boutoncroix=tk.Button()

canvas = tk.Canvas(fenetre,width=600,height=500,background="black")
canvas.grid(rows=1,column=1,rowspan=3)

def disque():
    x= randint(50,600-50)
    y = randint(50,400-50)
    canvas.create_oval(x-50,y+50,x+50,y-50,fill=couleur)

def rectangle():
    x= randint(50,600-50)
    y = randint(50,400-50)
    canvas.create_rectangle(x-50,y+50,x+50,y-50,fill=couleur)

def couleurfct():
    global couleur
    couleur = input("Entrez un couleur")

fenetre.mainloop()