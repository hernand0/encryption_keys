# Diego Hernando 2023

import string as st

def enc(list):
    lista = []
    listilla = []
    a = st.ascii_letters
    
    for i in list:
        lista.append(i)
    for i in a:
        listilla.append(i)
    for i in range(len(lista)):
        c = lista[i]
        if lista[i] == ' ':
            print(' ',end='')
        elif lista[i] in listilla:
            f = listilla.index(c)
            g = listilla[f+3]
            print(g.lower(), end='')
        else: continue
    print()

def dec(list):
    lista = []
    listilla = []
    a = st.ascii_letters
    
    for i in list:
        lista.append(i)
    for i in a:
        listilla.append(i)
    for i in range(len(lista)):
        c = lista[i]
        if lista[i] == ' ':
            print(' ',end='')
        elif lista[i] in listilla:
            f = listilla.index(c)
            g = listilla[f-3]
            print(g.lower(), end='')
        else: continue
    print()
    return
    
a = input('\nEscribe para encriptar:\n')
enc(a)
b = input('\nEscribe para desencriptar:\n')
dec(b)