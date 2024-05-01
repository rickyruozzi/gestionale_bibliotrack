import customtkinter as ctk
import mysql.connector

def espelli_utente():
    username = username_entry.get()
    if not username:
        show_error("Errore", "Inserire un username valido.")
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
    show_info("Successo", "Utente espulso con successo.")

def modifica_utente():
    campo = campo_entry.get()
    valore = valore_entry.get()
    username = username_entry.get()
    if not (campo and valore and username):
        show_error("Errore", "Inserire tutti i campi richiesti.")
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
    show_info("Successo", "Utente modificato con successo.")

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
        show_info("Nessun utente trovato", "Nessun utente trovato nel database.")
    else:
        users_info = "\n".join([f"Username: {data[0]}, Password: {data[1]}, Email: {data[2]}" for data in dati])
        show_info("Utenti", users_info)

def on_button_click(scelta):
    if scelta == '1':
        visualizza_utenti()
    elif scelta == '2':
        espelli_utente()
    elif scelta == '3':
        modifica_utente()

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

# Creazione dei widget
username_label = ctk.CTkLabel(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = ctk.CTkEntry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

campo_label = ctk.CTkLabel(root, text="Campo:")
campo_label.grid(row=1, column=0, padx=5, pady=5)
campo_entry = ctk.CTkEntry(root)
campo_entry.grid(row=1, column=1, padx=5, pady=5)

valore_label = ctk.CTkLabel(root, text="Valore:")
valore_label.grid(row=2, column=0, padx=5, pady=5)
valore_entry = ctk.CTkEntry(root)
valore_entry.grid(row=2, column=1, padx=5, pady=5)

scelta_label = ctk.CTkLabel(root, text="Quale operazione vuoi eseguire:")
scelta_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Bottone per visualizzare gli utenti
visualizza_button = ctk.CTkButton(root, text="Visualizzare gli utenti", command=lambda: on_button_click('1'))
visualizza_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per espellere un utente
espelli_button = ctk.CTkButton(root, text="Espellere un utente", command=lambda: on_button_click('2'))
espelli_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per modificare un utente
modifica_button = ctk.CTkButton(root, text="Modificare un utente", command=lambda: on_button_click('3'))
modifica_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Esecuzione del loop principale
root.mainloop()
