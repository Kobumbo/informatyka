plik = open('slowa.txt', 'r')

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

def a():
    ile = 0
    for i in lista:
        if i.count('0') > i.count('1'):
            ile += 1
    print(ile)

def czy_warunek(wyraz):
    return wyraz.rstrip('1')

def b():
    ile = 0
    for i in lista:
        if czy_warunek(i).count('1') == 0 and i.count('1') > 0 and i.count('0') > 0:
            ile += 1
    print(ile)
