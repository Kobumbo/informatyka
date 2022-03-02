plik = open('NAPIS.TXT', 'r')

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

def suma_kodow(tekst):
    suma = 0
    for i in tekst:
        suma += ord(i)
    return suma

def czy_rosnacy(tekst):
    for i in range(len(tekst)-1):
        if ord(tekst[i]) >= ord(tekst[i+1]):
            return False
    return True


def a():
    ile = 0
    for i in lista:
        if czy_pierwsza(suma_kodow(i)):
            ile += 1
    print(ile)

def b():
    for i in lista:
        if(czy_rosnacy(i)):
            print(i)

def c():
    lista2 = []
    for i in lista:
        if lista.count(i) > 1:
            if i not in lista2:
                lista2.append(i)
    for i in lista2:
        print(i)



