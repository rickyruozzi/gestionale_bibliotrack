import tkinter as tk
from tkinter import messagebox
import mysql.connector

def espelli_utente():
    username = username_entry.get()
    if not username:
        messagebox.showerror("Errore", "Inserire un username valido.")
        return
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Ruozzi1234',
        database='bibliotrack'
    )
    cur = conn.cursor()
    query = "DELETE FROM users WHERE username=%s"
    values = (username,)
    cur.execute(query, values)
    conn.commit()
    conn.close()
    messagebox.showinfo("Successo", "Utente espulso con successo.")

def modifica_utente():
    campo = campo_entry.get()
    valore = valore_entry.get()
    username = username_entry.get()
    if not (campo and valore and username):
        messagebox.showerror("Errore", "Inserire tutti i campi richiesti.")
        return
    query = f"UPDATE users SET {campo}=%s WHERE username=%s"
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Ruozzi1234",
        database="bibliotrack",
        port=3306,
    )
    cur = conn.cursor()
    cur.execute(query, (valore, username))
    conn.commit()
    conn.close()
    messagebox.showinfo("Successo", "Utente modificato con successo.")

def visualizza_utenti():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Ruozzi1234',
        database='bibliotrack'
    )
    cur = conn.cursor()
    query = "SELECT * FROM users"
    cur.execute(query)
    dati = cur.fetchall()
    conn.close()
    if not dati:
        messagebox.showinfo("Nessun utente trovato", "Nessun utente trovato nel database.")
    else:
        messagebox.showinfo("Utenti", "\n".join([f"Username: {data[0]}, Password: {data[1]}, Email: {data[2]}" for data in dati]))

def on_button_click(scelta):
    if scelta == '1':
        visualizza_utenti()
    elif scelta == '2':
        espelli_utente()
    elif scelta == '3':
        modifica_utente()

# Creazione della finestra principale
root = tk.Tk()
root.title("Gestionale BiblioTrack")

# Creazione dei widget
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

campo_label = tk.Label(root, text="Campo:")
campo_label.grid(row=1, column=0, padx=5, pady=5)
campo_entry = tk.Entry(root)
campo_entry.grid(row=1, column=1, padx=5, pady=5)

valore_label = tk.Label(root, text="Valore:")
valore_label.grid(row=2, column=0, padx=5, pady=5)
valore_entry = tk.Entry(root)
valore_entry.grid(row=2, column=1, padx=5, pady=5)

scelta_label = tk.Label(root, text="Quale operazione vuoi eseguire:")
scelta_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Bottone per visualizzare gli utenti
visualizza_button = tk.Button(root, text="Visualizzare gli utenti", command=lambda: on_button_click('1'))
visualizza_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per espellere un utente
espelli_button = tk.Button(root, text="Espellere un utente", command=lambda: on_button_click('2'))
espelli_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per modificare un utente
modifica_button = tk.Button(root, text="Modificare un utente", command=lambda: on_button_click('3'))
modifica_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Esecuzione del loop principale
root.mainloop()
