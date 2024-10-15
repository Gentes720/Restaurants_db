import sqlite3
import tkinter as tk
from tkinter import*
from tkinter import messagebox


conn = sqlite3.connect("restaurants.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            localisation TEXT,
            type TEXT,
            note INTEGER)
            """)

def insert_data():
    id = ligne_id.get()
    nom = ligne_nom.get()
    localisation = ligne_loc.get()
    type = ligne_type.get()
    note = ligne_note.get()

    if nom and localisation and type and note:
        cur.execute('''INSERT INTO restaurants
        (id, nom, localisation, type, note)
        VALUES(?, ?, ?, ?, ?)''',(id, nom, localisation, type, note))
        conn.commit()
        messagebox.showinfo("success")
        ligne_id.delete(0, tk.END)
        ligne_nom.delete(0, tk.END)
        ligne_loc.delete(0, tk.END)
        ligne_type.delete(0, tk.END)
        ligne_note.delete(0, tk.END)
    else:
        messagebox.showerror('Erreur')

fenetre = Tk()

fenetre.title ('Informations des restaurants')
id_label = Label(fenetre, text=" id du restaurant")
id_label.pack()
ligne_id = Entry(fenetre, width= 30)
ligne_id.pack()

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

bouton_insert = Button(fenetre, text='Inscrire', command=insert_data)
bouton_insert.pack()
fenetre.mainloop()


conn.close()            