import math

lista = [i.strip() for i in open('ciagi.txt', 'r')]

def rozklad(liczba):
    czynniki = []
    while liczba % 2 == 0:
        czynniki.append(liczba)
        liczba = liczba / 2
    for i in range(3, int(math.sqrt(liczba)) + 1 , 2):
        while liczba % i == 0:
            czynniki.append(i)
            liczba = liczba / i
    if liczba > 2:
        czynniki.append(liczba)
    return czynniki

def a():
    for i in lista:
        if len(i) % 2 == 0:
            if i[:len(i)//2] == i[len(i)//2:]:
                print(i)

def b():
    ile = 0
    for i in lista:
        czy_obok = False
        for j in range(len(i)-1):
            if i[j] == i[j+1] == '1':
                czy_obok = True
        if not czy_obok:
            ile += 1
    print(ile)

def c():
    liczby_polpierwsze = []
    for i in lista:
        if len(rozklad(int(i,2))) == 2:
            liczby_polpierwsze.append(int(i,2))
    print(len(liczby_polpierwsze))
    print(max(liczby_polpierwsze))
    print(min(liczby_polpierwsze))

