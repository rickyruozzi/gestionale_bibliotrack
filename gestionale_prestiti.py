import mysql.connector
from prettytable import PrettyTable

def switch(s):
    if s=='A':
        utente=input("inserire l'utente per il prestito: ")
        autore=input("inserisci il libro oggetto del prestito:  ")
        scadenza=input("inserire la scadenza del prestito: ")
        inizio=input("inserisci la data di inizio del prestito: ")
        conn=mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Ruozzi1234',
            database='bibliotrack'   
        )
        cur=conn.cursor()
        query = "INSERT INTO prestiti(FK_Id_utente,FK_Id_libro,scadenza_prestito,inizio_prestito) VALUES (%s,%s,%s,%s) "
        values=(utente, autore, scadenza, inizio)
        cur.execute(query,values)
        conn.commit()
        conn.close()
        print('dati aggiunti\n')
    if s=='D':
        id=int(input('inserire id del prestito da eliminare: '))
        conn=mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Ruozzi1234',
            database='bibliotrack'   
        )
        cur=conn.cursor()
        query = "DELETE FROM prestiti WHERE PK_Id_prestito=%s"
        values = (id,)
        cur.execute(query, values)
        conn.commit()
        conn.close()
        print('dati eliminati\n')
    if s=='M':
        campo=input('inserire il campo da modificare: ')
        valore=input('inserire il nuovo valore: ')
        if campo=='Anno_pubblicazione':
            valore=int(valore)
        id=input("inserire id dell'elemento da modificare: ")
        id=int(id)
        query = f"UPDATE prestiti SET {campo}=%s WHERE PK_Id_prestito=%s"
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Ruozzi1234",
            database="bibliotrack",
            port=3306,
            )
        cur = conn.cursor()
        cur.execute(query,(valore,id))
        conn.commit()
        conn.close()
    if s=='V':
        conn=mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Ruozzi1234',
            database='bibliotrack'   
        )
        cur=conn.cursor()
        query = "select * from prestiti"
        cur.execute(query)
        dati=cur.fetchall()
        # print(dati)
        if not dati:
            print("Nessun prestito trovato nel database.")
        else:
            for data in dati:
                print("ID_Persona:", data[1])
                print("ID_Libro:", data[2])
                print("scadenza:", data[3])
                print("inizio:", data[4])
                print('\n')
        conn.close()
        
if __name__=="__main__":
    print('benvenuto nel gestionale BiblioTrack!')
    scelta=''
    while scelta!='0':
        scelta=input('Quale operazione vuoi eseguire:\nA - aggiungi un prestito al database\nD - elimina un prestito dal database\nM - modifica un prestito nel database\nV - visualizzare i prestiti nel database\n0 - per uscire\n')
        while scelta!='A' and scelta!='D' and scelta!='M' and scelta!='V' and scelta!='0':
            scelta=input('Quale operazione vuoi eseguire:\nA - aggiungi un prestito al database\nD - elimina un prestito dal database\nM - modifica un prestito nel database\nV - visualizzare i prestiti nel database\n0 - per uscire\n')
        if scelta=='0': break
        switch(scelta)
    print('Arrivederci!')