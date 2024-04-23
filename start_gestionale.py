import subprocess 
import mysql.connector

def switch(scelta):
    if scelta=='1':
        exec(open("gestionale_catalogo.py").read())
    if scelta=='2':
        exec(open("gestionale_prestiti.py").read())
    else:
        print('opzione non ancora disponibile')

if __name__=='__main__':
    print('Benvenuto nel gestionale Bibliotrack, che cosa desidera fare?\n1 - Controllare o aggiornare il catalogo\n2 - controllare i prestiti attivi\n3 - gestire le tendenze\ninserire il valore corrispondente:')
    scelta=input()
    switch(scelta)