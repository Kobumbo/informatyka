import math

def zamiana_na_liczby(slowo):
    slowo = list(slowo)
    for i in range(len(slowo)):
        if slowo[i].isalpha():
            slowo[i] = ord(slowo[i]) - 65
    return slowo

def zamiana_na_litery(slowo):
    slowo = list(slowo)
    for i in range(len(slowo)):
        if str(slowo[i]).isnumeric():
            slowo[i] = chr(slowo[i] + 65)
    return slowo

def szyfrowanie(slowo, klucz):
    slowo = zamiana_na_liczby(slowo)
    while len(slowo) > len(klucz):
        klucz += klucz
    klucz = zamiana_na_liczby(klucz)
    indeks_klucza = 0
    for i in range(len(slowo)):
        if str(slowo[i]).isnumeric():
            if slowo[i] + klucz[indeks_klucza] > 25:
                slowo[i] = (slowo[i] + klucz[indeks_klucza]) % 26
            else:
                slowo[i] += klucz[indeks_klucza]
            indeks_klucza += 1
    return ''.join(zamiana_na_litery(slowo))


def a():
    dokad = [i.strip() for i in open('dokad.txt', 'r')]
    klucz = 'LUBIMYCZYTAC'
    print(szyfrowanie(*dokad, klucz))
    ile = 0
    for i in dokad[0]:
        if i.isalpha():
            ile += 1
    ile_razy = math.ceil(ile / len(klucz))
    print('Ile razy:', ile_razy)

def b():
    dokad = [i.strip() for i in open('szyfr.txt', 'r')]
    klucz = dokad[1]
    klucz = list(klucz)
    for i in range(len(klucz)):
        klucz[i] = (26 - zamiana_na_liczby(klucz[i])[0]) % 26
    klucz = ''.join(zamiana_na_litery(klucz))
    print(szyfrowanie(dokad[0], klucz))

def c():
    dokad = [i.strip() for i in open('szyfr.txt', 'r')]
    ilosc_liter = [0]*26
    n = 0
    for i in dokad[0]:
        if i.isalpha():
            n += 1
    for i in dokad[0]:
        if i.isalpha():
            ilosc_liter[ord(i) - 65] += 1
    for i in range(len(ilosc_liter)):
        print(chr(i+65), '-', ilosc_liter[i])
    suma = 0
    for i in range(26):
        suma += ilosc_liter[i] * (ilosc_liter[i] - 1)
    k = suma / (n * (n - 1))
    d = 0.0285 / (k - 0.0385)
    print('Szacunkowa dlugosc:', round(d,2))
    print('Rzeczywista dlugosc:', len(dokad[1]))
