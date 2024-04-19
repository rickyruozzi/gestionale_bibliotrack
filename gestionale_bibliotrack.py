import mysql.connector
from prettytable import PrettyTable

def switch(s):
    if s=='A':
        titolo=input('inserisci il titolo del libro: ')
        autore=input("inserisci l'autore del libro: ")
        genere=input('inserisci il genere del libro: ')
        casa_editrice=input('inserisci la casa editrice del libro: ')
        anno_pubblicazione=int(input("inserisci l'anno di pubblicazione de libro: "))
        collana=input('inserisci la collana del libro: ')
        conn=mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Ruozzi1234',
            database='bibliotrack'   
        )
        cur=conn.cursor()
        query = "INSERT INTO libri(Titolo,Autore,Casa_editrice,Anno_pubblicazione,Collana,Genere) VALUES (%s,%s,%s,%s,%s,%s) "
        values=(titolo,autore,casa_editrice,anno_pubblicazione,collana,genere)
        cur.execute(query,values)
        conn.commit()
        conn.close()
        print('dati aggiunti\n')
    if s=='D':
        id=int(input('inserire id del libro da eliminare: '))
        conn=mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Ruozzi1234',
            database='bibliotrack'   
        )
        cur=conn.cursor()
        query = "DELETE FROM libri WHERE PK_Id_libro=%s"
        values = (id,)
        cur.execute(query, values)
        conn.commit()
        conn.close()
        print('dati eliminati\n')
    if s=='M':
        print('Modifica')
    if s=='V':
        conn=mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Ruozzi1234',
            database='bibliotrack'   
        )
        cur=conn.cursor()
        query = "select * from libri"
        cur.execute(query)
        dati=cur.fetchall()
        # print(dati)
        if not dati:
            print("Nessun libro trovato nel database.")
        else:
            for data in dati:
                print("ID:", data[0])
                print("Titolo:", data[1])
                print("Autore:", data[2])
                print("Genere:", data[3])
                print("Casa editrice:", data[4])
                print("Anno di pubblicazione:", data[5])
                print("Collana:", data[6])
                print("\n")
        conn.close()
        
if __name__=="__main__":
    print('benvenuto nel gestionle BiblioTrack!')
    scelta=''
    while scelta!='0':
        scelta=input('Quale operazione vuoi eseguire:\nA - aggiungi un libro al database\nD - elimina un libro dal database\nM - modifica un libro nel database\nV - visualizzare i libri nel database\n0 - per uscire\n')
        while scelta!='A' and scelta!='D' and scelta!='M' and scelta!='V' and scelta!='0':
            scelta=input('Quale operazione vuoi eseguire:\nA - aggiungi un libro al database\nD - elimina un libro dal database\nM - modifica un libro nel database\nV - visualizzare i libri nel database\n0 - per uscire\n')
        if scelta=='0': break
        switch(scelta)
    print('Arrivederci!')