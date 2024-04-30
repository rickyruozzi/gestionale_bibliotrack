import tkinter as tk
from tkinter import messagebox
import mysql.connector
import prettytable

def aggiungi_prestito():
    utente = utente_entry.get()
    libro = libro_entry.get()
    scadenza = scadenza_entry.get()
    inizio = inizio_entry.get()
    
    if not (utente and libro and scadenza and inizio):
        messagebox.showerror("Errore", "Inserire tutti i campi richiesti.")
        return
    
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Ruozzi1234',
        database='bibliotrack'
    )
    cur = conn.cursor()
    query = "INSERT INTO prestiti(FK_Id_utente, FK_Id_libro, scadenza_prestito, inizio_prestito) VALUES (%s, %s, %s, %s)"
    values = (utente, libro, scadenza, inizio)
    cur.execute(query, values)
    conn.commit()
    conn.close()
    messagebox.showinfo("Successo", "Prestito aggiunto con successo.")

def elimina_prestito():
    id_prestito = id_entry.get()
    
    if not id_prestito:
        messagebox.showerror("Errore", "Inserire l'ID del prestito da eliminare.")
        return
    
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Ruozzi1234',
        database='bibliotrack'
    )
    cur = conn.cursor()
    query = "DELETE FROM prestiti WHERE PK_Id_prestito=%s"
    values = (id_prestito,)
    cur.execute(query, values)
    conn.commit()
    conn.close()
    messagebox.showinfo("Successo", "Prestito eliminato con successo.")

def modifica_prestito():
    campo = campo_entry.get()
    valore = valore_entry.get()
    id_prestito = id_entry.get()
    
    if not (campo and valore and id_prestito):
        messagebox.showerror("Errore", "Inserire tutti i campi richiesti.")
        return
    
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Ruozzi1234',
        database='bibliotrack'
    )
    cur = conn.cursor()
    query = f"UPDATE prestiti SET {campo}=%s WHERE PK_Id_prestito=%s"
    values = (valore, id_prestito)
    cur.execute(query, values)
    conn.commit()
    conn.close()
    messagebox.showinfo("Successo", "Prestito modificato con successo.")

def visualizza_prestiti():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Ruozzi1234',
        database='bibliotrack'
    )
    cur = conn.cursor()
    query = "SELECT * FROM prestiti"
    cur.execute(query)
    dati = cur.fetchall()
    conn.close()
    
    
    if not dati:
        messagebox.showinfo("Nessun prestito trovato", "Nessun prestito trovato nel database.")
    else:
        result=""
        for row in dati:
            result += f"ID Prestito: {row[0]}\nID Utente: {row[1]}\nID Libro: {row[2]}\nScadenza: {row[3]}\nInizio: {row[4]}\n\n"
        messagebox.showinfo("Prestiti", result)

def on_button_click(scelta):
    if scelta == 'A':
        aggiungi_prestito()
    elif scelta == 'D':
        elimina_prestito()
    elif scelta == 'M':
        modifica_prestito()
    elif scelta == 'V':
        visualizza_prestiti()

# Creazione della finestra principale
root = tk.Tk()
root.title("Gestionale BiblioTrack")

# Creazione dei widget
utente_label = tk.Label(root, text="Utente:")
utente_label.grid(row=0, column=0, padx=5, pady=5)
utente_entry = tk.Entry(root)
utente_entry.grid(row=0, column=1, padx=5, pady=5)

libro_label = tk.Label(root, text="Libro:")
libro_label.grid(row=1, column=0, padx=5, pady=5)
libro_entry = tk.Entry(root)
libro_entry.grid(row=1, column=1, padx=5, pady=5)

scadenza_label = tk.Label(root, text="Scadenza:")
scadenza_label.grid(row=2, column=0, padx=5, pady=5)
scadenza_entry = tk.Entry(root)
scadenza_entry.grid(row=2, column=1, padx=5, pady=5)

inizio_label = tk.Label(root, text="Inizio:")
inizio_label.grid(row=3, column=0, padx=5, pady=5)
inizio_entry = tk.Entry(root)
inizio_entry.grid(row=3, column=1, padx=5, pady=5)

id_label = tk.Label(root, text="ID Prestito:")
id_label.grid(row=4, column=0, padx=5, pady=5)
id_entry = tk.Entry(root)
id_entry.grid(row=4, column=1, padx=5, pady=5)

campo_label = tk.Label(root, text="Campo:")
campo_label.grid(row=5, column=0, padx=5, pady=5)
campo_entry = tk.Entry(root)
campo_entry.grid(row=5, column=1, padx=5, pady=5)

valore_label = tk.Label(root, text="Valore:")
valore_label.grid(row=6, column=0, padx=5, pady=5)
valore_entry = tk.Entry(root)
valore_entry.grid(row=6, column=1, padx=5, pady=5)

# Bottone per aggiungere un prestito
aggiungi_button = tk.Button(root, text="Aggiungi prestito", command=lambda: on_button_click('A'))
aggiungi_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per eliminare un prestito
elimina_button = tk.Button(root, text="Elimina prestito", command=lambda: on_button_click('D'))
elimina_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per modificare un prestito
modifica_button = tk.Button(root, text="Modifica prestito", command=lambda: on_button_click('M'))
modifica_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per visualizzare i prestiti
visualizza_button = tk.Button(root, text="Visualizza prestiti", command=lambda: on_button_click('V'))
visualizza_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Esecuzione del loop principale
root.mainloop()

