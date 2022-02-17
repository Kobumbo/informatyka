import math
plik = open("liczby.txt", "r")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].split()

def czy_rosnaco(lista = []):
    if int(lista[0]) < int(lista[1]) < int(lista[2]):
        return True
    return False

def suma_cyf_w_wierszu(lista = []):
    suma = 0
    for i in lista:
        for j in i:
            suma += int(j)
    return suma

def a():
    ile_wierszy = 0
    for i in lista:
        if czy_rosnaco(i):
            ile_wierszy += 1
    print(ile_wierszy)

def b():
    suma = 0
    for i in lista:
        suma += math.gcd(int(i[0]), int(i[1]), int(i[2]))
    print(suma)

def c():
    ilosc_35 = 0
    lista2 = []
    ilosc_max = 0
    for i in lista:
        if suma_cyf_w_wierszu(i) == 35:
            ilosc_35 += 1
    for i in lista:
        lista2.append(suma_cyf_w_wierszu(i))
    for i in lista:
        if suma_cyf_w_wierszu(i) == max(lista2):
            ilosc_max += 1
    print(f'Ilosc wierszy, gdzie suma = 35: {ilosc_35}')
    print(f'Najwieksza suma: {max(lista2)}, ilość: {ilosc_max}')
    