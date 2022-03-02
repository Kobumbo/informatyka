plik = open('dane.txt', 'r')

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

def zamiana_z_osemkowego(liczba):
    return str(int(liczba, 8))

def czy_mniejsza(liczba):
    maximum = liczba[0]
    for i in range(len(liczba)):
        if liczba[i] < maximum:
            return False
        maximum = liczba[i]
    return True

def a():
    ile_liczb = 0
    for i in lista:
        if i[0] == i[len(i)-1]:
            ile_liczb += 1
    print(ile_liczb)

def b():
    ile_liczb = 0
    for i in lista:
        if zamiana_z_osemkowego(i)[0] == zamiana_z_osemkowego(i)[len(zamiana_z_osemkowego(i))-1]:
            ile_liczb += 1
    print(ile_liczb)

def c():
    lista2 = []
    ile = 0
    for i in range(len(lista)):
        if czy_mniejsza(lista[i]):
            ile += 1
            lista2.append(int(lista[i]))
    print(ile)
    print(f'{max(lista2)} - max')   
    print(f'{min(lista2)} - min') 

