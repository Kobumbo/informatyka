plik = open("dane_6.txt", "r")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

def czy_pierwsza(liczba):
    i = 2
    if liczba < 2:
        return False
    while i < liczba:
        if liczba % i == 0:
            return False
        i += 1
    return True