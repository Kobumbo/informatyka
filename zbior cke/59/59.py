plik = open('liczby.txt', 'r')

lista = plik.readlines()

for i in range(len(lista)):
    lista[i] = lista[i].strip()


def rozklad(liczba):
    czynniki = []
    x = 2
    if liczba % 2 == 0:
        return 0
    while liczba >= 2:
        while liczba % x == 0:
            liczba //= x
            if x not in czynniki:
                czynniki.append(x)
            if len(czynniki) > 3:
                return 0
        x += 1
    return len(czynniki)


def a():
    ile = 0
    for i in lista:
        if rozklad(int(i)) == 3:
            ile += 1
            print(ile)
    print('Koniec')
    print(ile)
    print('Koniec')


def b():
    ile = 0
    for i in lista:
        if str(int(i) + int(i[::-1])) == str(int(i) + int(i[::-1]))[::-1]:
            ile += 1
    print(ile)


# a()
b()
