import customtkinter as ctk
import mysql.connector

def aggiungi_libro():
    titolo = titolo_entry.get()
    autore = autore_entry.get()
    genere = genere_entry.get()
    casa_editrice = casa_editrice_entry.get()
    anno_pubblicazione = anno_pubblicazione_entry.get()
    collana = collana_entry.get()
    
    if not (titolo and autore and genere and casa_editrice and anno_pubblicazione and collana):
        show_error("Errore", "Inserire tutti i campi richiesti.")
        return
    
    try:
        anno_pubblicazione = int(anno_pubblicazione)
    except ValueError:
        show_error("Errore", "L'anno di pubblicazione deve essere un numero intero.")
        return
    
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Ruozzi1234',
        database='bibliotrack'
    )
    cur = conn.cursor()
    query = "INSERT INTO libri(Titolo, Autore, Casa_editrice, Anno_pubblicazione, Collana, Genere) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (titolo, autore, casa_editrice, anno_pubblicazione, collana, genere)
    cur.execute(query, values)
    conn.commit()
    conn.close()
    show_info("Successo", "Libro aggiunto con successo.")

def elimina_libro():
    id_libro = id_entry.get()
    
    if not id_libro:
        show_error("Errore", "Inserire l'ID del libro da eliminare.")
        return
    
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Ruozzi1234',
        database='bibliotrack'
    )
    cur = conn.cursor()
    query = "DELETE FROM libri WHERE PK_Id_libro=%s"
    values = (id_libro,)
    cur.execute(query, values)
    conn.commit()
    conn.close()
    show_info("Successo", "Libro eliminato con successo.")

def modifica_libro():
    campo = campo_entry.get()
    valore = valore_entry.get()
    id_libro = id_entry.get()
    
    if not (campo and valore and id_libro):
        show_error("Errore", "Inserire tutti i campi richiesti.")
        return
    
    try:
        id_libro = int(id_libro)
    except ValueError:
        show_error("Errore", "L'ID del libro deve essere un numero intero.")
        return
    
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Ruozzi1234',
        database='bibliotrack'
    )
    cur = conn.cursor()
    query = f"UPDATE libri SET {campo}=%s WHERE PK_Id_libro=%s"
    values = (valore, id_libro)
    cur.execute(query, values)
    conn.commit()
    conn.close()
    show_info("Successo", "Libro modificato con successo.")

def visualizza_libri():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Ruozzi1234',
        database='bibliotrack'
    )
    cur = conn.cursor()
    query = "SELECT * FROM libri"
    cur.execute(query)
    dati = cur.fetchall()
    conn.close()
    
    if not dati:
        show_info("Nessun libro trovato", "Nessun libro trovato nel database.")
    else:
        result = "ID\tTitolo\tAutore\tGenere\tCasa editrice\tAnno pubblicazione\tCollana\n"
        for row in dati:
            result += "\t".join(map(str, row)) + "\n"
        show_info("Libri", result)

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
titolo_label = ctk.CTkLabel(root, text="Titolo:")
titolo_label.grid(row=0, column=0, padx=5, pady=5)
titolo_entry = ctk.CTkEntry(root)
titolo_entry.grid(row=0, column=1, padx=5, pady=5)

autore_label = ctk.CTkLabel(root, text="Autore:")
autore_label.grid(row=1, column=0, padx=5, pady=5)
autore_entry = ctk.CTkEntry(root)
autore_entry.grid(row=1, column=1, padx=5, pady=5)

genere_label = ctk.CTkLabel(root, text="Genere:")
genere_label.grid(row=2, column=0, padx=5, pady=5)
genere_entry = ctk.CTkEntry(root)
genere_entry.grid(row=2, column=1, padx=5, pady=5)

casa_editrice_label = ctk.CTkLabel(root, text="Casa editrice:")
casa_editrice_label.grid(row=3, column=0, padx=5, pady=5)
casa_editrice_entry = ctk.CTkEntry(root)
casa_editrice_entry.grid(row=3, column=1, padx=5, pady=5)

anno_pubblicazione_label = ctk.CTkLabel(root, text="Anno pubblicazione:")
anno_pubblicazione_label.grid(row=4, column=0, padx=5, pady=5)
anno_pubblicazione_entry = ctk.CTkEntry(root)
anno_pubblicazione_entry.grid(row=4, column=1, padx=5, pady=5)

collana_label = ctk.CTkLabel(root, text="Collana:")
collana_label.grid(row=5, column=0, padx=5, pady=5)
collana_entry = ctk.CTkEntry(root)
collana_entry.grid(row=5, column=1, padx=5, pady=5)

id_label = ctk.CTkLabel(root, text="ID Libro:")
id_label.grid(row=6, column=0, padx=5, pady=5)
id_entry = ctk.CTkEntry(root)
id_entry.grid(row=6, column=1, padx=5, pady=5)

campo_label = ctk.CTkLabel(root, text="Campo:")
campo_label.grid(row=7, column=0, padx=5, pady=5)
campo_entry = ctk.CTkEntry(root)
campo_entry.grid(row=7, column=1, padx=5, pady=5)

valore_label = ctk.CTkLabel(root, text="Valore:")
valore_label.grid(row=8, column=0, padx=5, pady=5)
valore_entry = ctk.CTkEntry(root)
valore_entry.grid(row=8, column=1, padx=5, pady=5)

# Bottone per aggiungere un libro
aggiungi_button = ctk.CTkButton(root, text="Aggiungi libro", command=aggiungi_libro)
aggiungi_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per eliminare un libro
elimina_button = ctk.CTkButton(root, text="Elimina libro", command=elimina_libro)
elimina_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per modificare un libro
modifica_button = ctk.CTkButton(root, text="Modifica libro", command=modifica_libro)
modifica_button.grid(row=11, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Bottone per visualizzare i libri
visualizza_button = ctk.CTkButton(root, text="Visualizza libri", command=visualizza_libri)
visualizza_button.grid(row=12, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Avvio dell'applicazione
root.mainloop()
