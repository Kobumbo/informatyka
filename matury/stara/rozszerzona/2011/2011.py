plik = open('liczby.txt', 'r')

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

def suma_cyfr(liczba):
    suma = 0
    for i in range(len(liczba)):
        suma += int(liczba[i])
    return suma

def a():
    ile_parzystych = 0
    for i in lista:
        if int(i) % 2 == 0:
            ile_parzystych += 1
    print(ile_parzystych)

def b():
    lista2 = []
    for i in lista:
        lista2.append(int(i))
    print(f'{max(lista2)} - system dwójkowy')
    print(f'{int(str(max(lista2)), 2)} - system dziesiętny')

def c():
    ile_liczb = 0
    suma = 0
    for i in lista:
        if len(i) == 9:
            ile_liczb += 1
            suma += int(i, 2)
    print(f'Ile liczb: {ile_liczb}')
    print(f'Suma liczb: {bin(suma)[2:]}')


