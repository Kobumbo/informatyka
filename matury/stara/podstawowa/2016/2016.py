from subprocess import list2cmdline


plik = open("dane_6.txt", "r")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

def a():
    ile_pierwszych = 0
    for i in lista:
        if czy_pierwsza(int(i)):
            ile_pierwszych += 1
    print(ile_pierwszych)

def b():
    lista2 = []
    for i in lista:
        if czy_pierwsza(int(i)):
            lista2.append(int(i))
    print(max(lista2))
    print(min(lista2))

def c():
    ile_par = 0
    lista2 = []
    for i in lista:
        if czy_pierwsza(int(i)):
            lista2.append(int(i))
    for i in range(len(lista2)-1):
        if abs(lista2[i] - lista2[i+1]) == 2:
            ile_par += 1
            print(f'{lista2[i]} {lista2[i+1]}')
    print(f'{ile_par} pary')
