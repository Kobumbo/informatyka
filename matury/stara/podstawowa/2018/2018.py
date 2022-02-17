plik = open("liczby.txt", "r")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

def suma_wszystkich_cyfr():
    suma = 0
    for i in lista:
        for j in i:
            suma += int(j)
    print(f'Suma wszystkich cyfr: {suma}')

def suma_cyfr(liczba):
    suma = 0
    for i in range(len(liczba)):
        suma += int(liczba[i])
    return suma

def a():
    lista_parzyste = []
    for i in lista:
        if int(i) % 2 == 0:
            lista_parzyste.append(int(i))
    print(max(lista_parzyste))

def b():
    for i in lista:
        if i == i[::-1]:
            print(i)

def c():
    for i in lista:
        if suma_cyfr(i) > 30:
            print(i)
    suma_wszystkich_cyfr()