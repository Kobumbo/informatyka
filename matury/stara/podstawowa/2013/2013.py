plik = open("napisy.txt", "r")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()


def a():
    ile_parzysta_dlugosc = 0
    for i in lista:
        if len(i) % 2 == 0:
            ile_parzysta_dlugosc += 1
    print(ile_parzysta_dlugosc)


def b():
    ilosc_wyrazow = 0
    for i in lista:
        if i.count('0') == i.count('1'):
            ilosc_wyrazow += 1
    print(ilosc_wyrazow)


def c():
    same_zera = 0
    same_jedynki = 0
    for i in lista:
        if i.count('0') == len(i):
            same_zera += 1
        elif i.count('1') == len(i):
            same_jedynki += 1   
    print(f'Zera: {same_zera}')
    print(f'Jedynki: {same_jedynki}')


def d():
    for k in range(2, 17):
        ilosc = 0
        for i in lista:
            if k == len(i):
                ilosc += 1
        print(f'k = {k}: {ilosc}')
