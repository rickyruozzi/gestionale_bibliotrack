import customtkinter as ctk
import subprocess 

def switch(scelta):
    if scelta == '1':
        subprocess.Popen(["python", "gestionale_catalogo.py"])  
    elif scelta == '2':
        subprocess.Popen(["python", "gestionale_prestiti.py"])
    elif scelta == '3':
        subprocess.Popen(["python", "gestionale_utenti.py"])
    else:
        show_error('Errore','Scelta non valida')

def show_error(title, message):
    error_window = ctk.CTk()
    error_window.title(title)
    
    error_label = ctk.CTkLabel(error_window, text=message, font=("Arial", 12))
    error_label.pack(pady=20)
    
    ok_button = ctk.CTkButton(error_window, text="OK", command=error_window.destroy)
    ok_button.pack(pady=10)
    
    error_window.mainloop()

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

# Creazione della finestra principale
root = ctk.CTk()
root.title("Gestionale Bibliotrack")
root.geometry("400x250")

# Creazione del frame
main_frame = ctk.CTkFrame(root)
main_frame.pack(expand=True, fill="both", padx=10, pady=10)

# Etichetta di benvenuto
welcome_label = ctk.CTkLabel(main_frame, text="Benvenuto nel gestionale Bibliotrack", font=("Arial", 14))
welcome_label.pack(pady=(0, 10))

# Etichetta delle opzioni
options_label = ctk.CTkLabel(main_frame, text="Cosa desidera fare?", font=("Arial", 12))
options_label.pack()

# Opzioni
options_text = "1 - Controllare o aggiornare il catalogo\n2 - Controllare i prestiti attivi\n3 - Gestire gli utenti"
options_display = ctk.CTkLabel(main_frame, text=options_text, font=("Arial", 12))
options_display.pack(pady=(0, 10))

# Casella di testo per l'inserimento della scelta
scelta_entry = ctk.CTkEntry(main_frame, font=("Arial", 12))
scelta_entry.pack(pady=(0, 10))

# Bottone per confermare la scelta
confirm_button = ctk.CTkButton(main_frame, text="Conferma", font=("Arial", 12), command=on_button_click)
confirm_button.pack()

# Esecuzione del loop principale
root.mainloop()

# Centra la finestra dopo il mainloop
center_window(root)
