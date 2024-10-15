import tkinter as tk
from tkinter import*

fenetre = Tk()

fenetre.title ('Informations des restaurants')
nom_label = Label(fenetre, text="le nom de votre restaurant")
nom_label.pack()
ligne_nom = Entry(fenetre, width= 30)
ligne_nom.pack()

loc_label = Label(fenetre, text="localisation du restaurant")
loc_label.pack()
ligne_loc = Entry(fenetre, width= 30)
ligne_loc.pack()

type_label = Label(fenetre, text="le type du restaurant")
type_label.pack()
ligne_type = Entry(fenetre, width= 30)
ligne_type.pack()

note_label = Label(fenetre, text="Note du restaurant sur 5")
note_label.pack()
ligne_note = Entry(fenetre, width= 30)
ligne_note.pack()

bouton_insert = Button(fenetre, text='Inscrire')
bouton_insert.pack()

fenetre.mainloop()