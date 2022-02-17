plik = open("slowa.txt", "r")
plik2 = open("nowe.txt", "r")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

lista2 = plik2.readlines()
for i in range(len(lista2)):
    lista2[i] = lista2[i].strip()

def a():
    for n in range(1,13):
        ilosc = 0
        for i in lista:
            if n == len(i):
                ilosc += 1
        print(f'n = {n}: {ilosc}') 

def b():
    for i in lista2:
        print(f'{i} {lista.count(i)} {lista.count(i[::-1])}')

a()
b()
