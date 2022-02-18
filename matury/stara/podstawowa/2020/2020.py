import math
plik = open("liczby.txt", "r")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

def suma_cyfr(liczba):
    suma = 0
    for i in range(len(liczba)):
        suma += int(liczba[i])
    return suma

def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, math.sqrt(liczba)+1):
        if liczba % i == 0:
            return False
    return liczba

def a():
    ile_nieparzystych = 0
    for i in lista:   
        if int(i) % 2 == 1:
            ile_nieparzystych += 1
    print(ile_nieparzystych)

def b():
    for i in lista:
        if suma_cyfr(i) == 11:
            print(i)    

def c():
    for i in lista:
        if 4000 <= czy_pierwsza(int(i)) <= 5000:
            print(czy_pierwsza(int(i)))
            