import tkinter as tk
from tkinter import*
import sqlite3

conn = sqlite3.connect("restaurants.db")
cur = conn.cursor()

fenetre = Tk()
fenetre.title("Liste des restaurants")
texte = Text(fenetre)
texte.pack()

def afficher():
    cur.execute("SELECT * FROM restaurants")
    donnees = cur.fetchall()
    texte.delete(1.0, tk.END)
    for donnee in donnees:
        texte.insert(tk.END, str(donnee) + "\n")
bouton = Button(fenetre, text='Afficher la liste', command= afficher)
bouton.pack()
fenetre.mainloop()
conn.close()
