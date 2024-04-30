import tkinter as tk
from tkinter import messagebox
import subprocess 
import mysql.connector

def switch(scelta):
    if scelta == '1':
        subprocess.Popen(["python", "gestionale_catalogo.py"])  #lanciamo un processo che esegua lo script nel linguaggio python
    elif scelta == '2':
        subprocess.Popen(["python", "gestionale_prestiti.py"])
    elif scelta == '3':
        subprocess.Popen(["python", "gestionale_utenti.py"])
    else:
        messagebox.showerror("Errore", "Scelta non valida") #stampa un errore con la sintassi di tkinter

def on_button_click():
    scelta = scelta_entry.get()
    switch(scelta)

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.deiconify()  # Per rendere visibile la finestra
    window.wait_visibility()  # Attendiamo che la finestra sia visibile prima di continuare


# Creazione della finestra principale
root = tk.Tk()  #istanza di una interfaccia tkinter
root.title("Gestionale Bibliotrack")    #titolo della scheda
root.geometry("400x250")    #dimensioni della scheda

# Creazione del frame
main_frame = tk.Frame(root, bg="white") #creazione della finestra
main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)    #informazioni sulla finestra

# Etichetta di benvenuto
welcome_label = tk.Label(main_frame, text="Benvenuto nel gestionale Bibliotrack", font=("Arial", 14), bg="white")  
welcome_label.pack(pady=(0, 10))    #etichetta di benvenuto

# Etichetta delle opzioni
options_label = tk.Label(main_frame, text="Cosa desidera fare?", font=("Arial", 12), bg="white")
options_label.pack()    #etichetta delle opzioni pt.1

# Opzioni
options_text = "1 - Controllare o aggiornare il catalogo\n2 - Controllare i prestiti attivi\n3 - Gestire gli utenti"
options_display = tk.Label(main_frame, text=options_text, font=("Arial", 12), bg="white", justify=tk.LEFT)
options_display.pack(pady=(0, 10)) #etichetta delle opzioni pt.2

# Casella di testo per l'inserimento della scelta
scelta_entry = tk.Entry(main_frame, font=("Arial", 12))
scelta_entry.pack(pady=(0, 10)) 

# Bottone per confermare la scelta
confirm_button = tk.Button(main_frame, text="Conferma", font=("Arial", 12), command=on_button_click)
confirm_button.pack()

# Esecuzione del loop principale
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    

# Altri elementi...

# Esecuzione del loop principale
center_window(root)
root.mainloop()
