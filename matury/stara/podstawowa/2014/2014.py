from math import gcd
import math
plik = open("PARY_LICZB.TXT", "r")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].split()

def suma_cyfr(cyfra):
    suma = 0
    for i in range(len(cyfra)):
        suma += int(cyfra[i])
    return suma

def a():
    ile_wierszy = 0
    for i in range(len(lista)):
        if int(lista[i][0]) % int(lista[i][1]) == 0 or int(lista[i][1]) % int(lista[i][0]) == 0:
            ile_wierszy += 1
    print(ile_wierszy)

def b():
    ile_wierszy = 0
    for i in range(len(lista)):
        if math.gcd(int(lista[i][0]), int(lista[i][1])) == 1:
            ile_wierszy += 1
    print(ile_wierszy)

def c():
    ile_wierszy = 0
    for i in range(len(lista)):
        if suma_cyfr(lista[i][0]) == suma_cyfr(lista[i][1]):
            ile_wierszy += 1
    print(ile_wierszy)