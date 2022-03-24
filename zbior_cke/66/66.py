lista = [i.split() for i in open('trojki.txt', 'r')]

for i in range(len(lista)):
    for j in range(len(lista[i])):
        lista[i][j] = int(lista[i][j])

def suma_cyfr(liczba):
    suma = 0
    for i in liczba:
        suma += int(i)
    return suma

def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

def czy_boki_trojkata(trojka):
    trojka = sorted(trojka)
    if trojka[0] + trojka[1] > trojka[2]:
        return True
    return False

def a():
    for i in lista:
        if suma_cyfr(str(i[0])) + suma_cyfr(str(i[1])) == i[2]:
            print(*i)

def b():
    for i in lista:
        if czy_pierwsza(i[0]) and czy_pierwsza(i[1]) and i[0] * i[1] == i[2]:
            print(*i)

def c():
    for i in range(len(lista) - 1):
        liczby = []
        liczby_1 = []
        for j in range(3):
            liczby.append(lista[i][j])
            liczby_1.append(lista[i + 1][j])
        liczby = sorted(liczby)
        liczby_1 = sorted(liczby_1)
        if liczby[0] ** 2 + liczby[1] ** 2 == liczby[2] ** 2 and liczby_1[0] ** 2 + liczby_1[1] ** 2 == liczby_1[2] ** 2:
            print(*lista[i], '|', *lista[i+1])

def d():
    dlugosc_ciagu = 0
    maksymalna_dlugosc_ciagu = 0
    ilosc_wierszy = 0
    for i in lista:
        if czy_boki_trojkata(i):
            dlugosc_ciagu +=1
            ilosc_wierszy += 1
            if dlugosc_ciagu > maksymalna_dlugosc_ciagu:
                maksymalna_dlugosc_ciagu = dlugosc_ciagu
        else:
            dlugosc_ciagu = 0
    print('ilosc wierszy', ilosc_wierszy)
    print('maksymalna dlugosc ciagu', maksymalna_dlugosc_ciagu)

c()