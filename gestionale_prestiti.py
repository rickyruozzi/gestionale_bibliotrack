import customtkinter as ctk
import mysql.connector

def aggiungi_prestito():
    utente = utente_entry.get()
    libro = libro_entry.get()
    scadenza = scadenza_entry.get()
    inizio = inizio_entry.get()
    
    if not (utente and libro and scadenza and inizio):
        show_error("Errore", "Inserire tutti i campi richiesti.")
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
    show_info("Successo", "Prestito aggiunto con successo.")

def elimina_prestito():
    id_prestito = id_entry.get()
    
    if not id_prestito:
        show_error("Errore", "Inserire l'ID del prestito da eliminare.")
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
    show_info("Successo", "Prestito eliminato con successo.")

def modifica_prestito():
    campo = campo_entry.get()
    valore = valore_entry.get()
    id_prestito = id_entry.get()
    
    if not (campo and valore and id_prestito):
        show_error("Errore", "Inserire tutti i campi richiesti.")
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
    show_info("Successo", "Prestito modificato con successo.")

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
        show_info("Nessun prestito trovato", "Nessun prestito trovato nel database.")
    else:
        prestiti_info = "\n".join([f"ID Prestito: {row[0]}, ID Utente: {row[1]}, ID Libro: {row[2]}, Scadenza: {row[3]}, Inizio: {row[4]}" for row in dati])
        show_info("Prestiti", prestiti_info)

def on_button_click(scelta):
    if scelta == 'A':
        aggiungi_prestito()
    elif scelta == 'D':
        elimina_prestito()
    elif scelta == 'M':
        modifica_prestito()
    elif scelta == 'V':
        visualizza_prestiti()

def show_info(title, message):
    info_window = ctk.CTk()
    info_window.title(title)
    
    info_label = ctk.CTkLabel(info_window, text=message, font=("Arial", 12))
    info_label.pack(pady=20)
    
    ok_button = ctk.CTkButton(info_window, text="OK", command=info_window.destroy)
    ok_button.pack(pady=10)
    
    info_window.mainloop()

def show_error(title, message):
    error_window = ctk.CTk()
    error_window.title(title)
    
    error_label = ctk.CTkLabel(error_window, text=message, font=("Arial", 12))
    error_label.pack(pady=20)
    
    ok_button = ctk.CTkButton(error_window, text="OK", command=error_window.destroy)
    ok_button.pack(pady=10)
    
    error_window.mainloop()

# Creazione della finestra principale
root = ctk.CTk()
root.title("Gestionale BiblioTrack")
root.geometry("300x500")

# Creazione dei widget
utente_label = ctk.CTkLabel(root, text="Utente:")
utente_label.grid(row=0, column=0, padx=5, pady=5)
utente_entry = ctk.CTkEntry(root)
utente_entry.grid(row=0, column=1, padx=5, pady=5)

libro_label = ctk.CTkLabel(root, text="Libro:")
libro_label.grid(row=1, column=0, padx=5, pady=5)
libro_entry = ctk.CTkEntry(root)
libro_entry.grid(row=1, column=1, padx=5, pady=5)

scadenza_label = ctk.CTkLabel(root, text="Scadenza:")
scadenza_label.grid(row=2, column=0, padx=5, pady=5)
scadenza_entry = ctk.CTkEntry(root)
scadenza_entry.grid(row=2, column=1, padx=5, pady=5)

inizio_label = ctk.CTkLabel(root, text="Inizio:")
inizio_label.grid(row=3, column=0, padx=5, pady=5)
inizio_entry = ctk.CTkEntry(root)
inizio_entry.grid(row=3, column=1, padx=5, pady=5)

id_label = ctk.CTkLabel(root, text="ID Prestito:")
id_label.grid(row=4, column=0, padx=5, pady=5)
id_entry = ctk.CTkEntry(root)
id_entry.grid(row=4, column=1, padx=5, pady=5)

campo_label = ctk.CTkLabel(root, text="Campo:")
campo_label.grid(row=5, column=0, padx=5, pady=5)
campo_entry = ctk.CTkEntry(root)
campo_entry.grid(row=5, column=1, padx=5, pady=5)

valore_label = ctk.CTkLabel(root, text="Valore:")
valore_label.grid(row=6, column=0, padx=5, pady=5)
valore_entry = ctk.CTkEntry(root)
valore_entry.grid(row=6, column=1, padx=5, pady=5)

# Bottone per aggiungere un prestito
aggiungi_button = ctk.CTkButton(root, text="Aggiungi prestito", command=lambda: on_button_click('A'))
aggiungi_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per eliminare un prestito
elimina_button = ctk.CTkButton(root, text="Elimina prestito", command=lambda: on_button_click('D'))
elimina_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per modificare un prestito
modifica_button = ctk.CTkButton(root, text="Modifica prestito", command=lambda: on_button_click('M'))
modifica_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per visualizzare i prestiti
visualizza_button = ctk.CTkButton(root, text="Visualizza prestiti", command=lambda: on_button_click('V'))
visualizza_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Esecuzione del loop principale
root.mainloop()
