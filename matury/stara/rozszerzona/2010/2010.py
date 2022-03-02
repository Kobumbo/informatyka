import math
import copy

plik = open("anagram.txt", "r")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].split()
lista2 = []
lista2 = copy.deepcopy(lista)

# for i in range(len(lista)):
#     print(lista[i])


    
def taka_sama_liczba_znakow(wiersz):
    for i in range(len(wiersz)):
        if len(wiersz[i]) != len(wiersz[0]):
            return False
    return True

def kazdy_element_listy_jednakowy(lista):
    element = lista[0]
    for i in lista:
        if element != i:
            return False
    return True

def a_1():
    plik2 = open("odp_4a.txt", "w")
    for i in lista:
        if taka_sama_liczba_znakow(i):
            for j in range(len(i)):
                print(i[j], end = ' ', file = plik2)
            print(file = plik2)


def b_1():
    for i in range(len(lista2)):
        for j in range(len(lista2[i])):
            lista2[i][j] = "".join(sorted(lista2[i][j]))
        if kazdy_element_listy_jednakowy(lista2[i]):
            print(lista[i])

def a():
    for i in lista:
        if len(i[0]) == len(i[1]) == len(i[2]) == len(i[3]) == len(i[4]):
            print(*i)

def liczenie_liter(wyraz):
    lista = [0]*26
    for i in wyraz:
            lista[ord(i)-ord('a')] += 1
    return lista

def b():
    for i in lista:
        if liczenie_liter(i[0]) == liczenie_liter(i[1]) == liczenie_liter(i[2]) == liczenie_liter(i[3]) == liczenie_liter(i[4]):
            print(i)

def usuwanie_lier():
    wyraz = list(lista[1])
    for litera in lista[0]:
        indeks = wyraz.index(litera)
        wyraz[indeks] = ''
    print(wyraz)
usuwanie_lier()

