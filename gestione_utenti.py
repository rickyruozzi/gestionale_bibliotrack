import mysql.connector

def switch(s):
    if s=='2':
        username=input("inserire username  dell'utente da eliminare: ")
        conn=mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Ruozzi1234',
            database='bibliotrack'   
        )
        cur=conn.cursor()
        query = "DELETE FROM users WHERE username=%s"
        values = (username,)
        cur.execute(query, values)
        conn.commit()
        conn.close()
        print('dati eliminati\n')
    if s=='3':
        campo=input('inserire il campo da modificare: ')
        valore=input('inserire il nuovo valore: ')
        username=input("inserire username dell'elemento da modificare: ")
        query = f"UPDATE users SET {campo}=%s WHERE username=%s"
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Ruozzi1234",
            database="bibliotrack",
            port=3306,
            )
        cur = conn.cursor()
        cur.execute(query,(valore,username))
        conn.commit()
        conn.close()
    if s=='1':
        conn=mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Ruozzi1234',
            database='bibliotrack'   
        )
        cur=conn.cursor()
        query = "select * from users"
        cur.execute(query)
        dati=cur.fetchall()
        # print(dati)
        if not dati:
            print("Nessun utente trovato nel database.")
        else:
            for data in dati:
                print("Username:", data[0])
                print("password:", data[1])
                print("email:", data[2])
                print('\n')
        conn.close()

if __name__=='__main__':
    print('benvenuto nel gestionale BiblioTrack!')
    scelta=''
    while scelta!='0':
        scelta=input('Quale operazione vuoi eseguire:\n1 - visualizzare gli utenti\n2 - espellere un utente\n3 - modificare un utente\n0 - per uscire\n')
        while scelta!='1' and scelta!='2' and scelta!='3' and scelta!='0':
            scelta=input('Quale operazione vuoi eseguire:\n1 - visualizzare gli utenti\n2 - espellere un utente\n3 - modificare un utente\n0 - per uscire\n')
        if scelta=='0': break
        switch(scelta)
    print('Arrivederci!')