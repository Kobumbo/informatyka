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

def dlugosc_bloku(wyraz):
    maximum = 0
    wyraz = wyraz.split('1')
    for i in wyraz:
        if i.count('0') > maximum:
            maximum = i.count('0')
    return maximum

def b():
    ile = 0
    for i in lista:
        if czy_warunek(i).count('1') == 0 and i.count('1') > 0 and i.count('0') > 0:
            ile += 1
    print(ile)

def c():
    lista2 = []
    for i in lista:
        lista2.append(dlugosc_bloku(i))
    print(f'{max(lista2)} - najdluzszy blok')
    for i in lista:
        if dlugosc_bloku(i) == max(lista2):
            print(i)
c()