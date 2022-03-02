plik1 = open('tj.txt', 'r')
plik2 = open('klucze1.txt', 'r')
plik3 = open('sz.txt', 'r')
plik4 = open('klucze2.txt', 'r')


lista1 = plik1.readlines()
lista2 = plik2.readlines()
lista3 = plik3.readlines()
lista4 = plik4.readlines()
for i in range(len(lista1)):
    lista1[i] = lista1[i].strip()
    lista2[i] = lista2[i].strip()
    lista3[i] = lista3[i].strip()
    lista4[i] = lista4[i].strip()

def szyfrowanie(tekst, klucz):
    zaszyfrowany_wyraz = ''
    while len(tekst) > len(klucz):
        klucz += klucz
    for i in range(len(tekst)):
        suma = ord(tekst[i]) + (ord(klucz[i])-64)
        if suma > 90:
            suma -= 26
        zaszyfrowany_wyraz += chr(suma)
    return zaszyfrowany_wyraz

def deszyfrowanie(tekst, klucz):
    zdeszyfrowany_wyraz = ''
    while len(tekst) > len(klucz):
        klucz += klucz
    for i in range(len(tekst)):
        suma = ord(tekst[i]) - (ord(klucz[i])-64)
        if suma < 65:
            suma += 26
        zdeszyfrowany_wyraz += chr(suma)
    return zdeszyfrowany_wyraz

def a():
    plik5 = open('wynik4a.txt', 'w')
    for i in range(len(lista1)):
        print(szyfrowanie(lista1[i], lista2[i]), file = plik5)

def b():
    plik6 = open('wynik4b.txt', 'w')
    for i in range(len(lista3)):
        print(deszyfrowanie(lista3[i], lista4[i]), file = plik6)