import math

lista = [i.split() for i in open('dane_ulamki.txt', 'r')]

for i in range(len(lista)):
    for j in range(len(lista[i])):
        lista[i][j] = int(lista[i][j])

def czy_skracalny(ulamek):
    if math.gcd(ulamek[0], ulamek[1]) == 1:
        return False
    return True

def skrocenie_ulamka(ulamek):
    nwd = math.gcd(ulamek[0], ulamek[1])
    ulamek[0] //= nwd
    ulamek[1] //= nwd
    return [ulamek[0], ulamek[1]]


def a():
    najmniejszy_ulamek = []
    najmniejsza_liczba = 12000
    najmniejszy_mianownik = 12000
    for i in range(len(lista)):
        if lista[i][0] / lista[i][1] < najmniejsza_liczba:
            najmniejsza_liczba = lista[i][0] / lista[i][1]
            najmniejszy_ulamek = [lista[i][0], lista[i][1]]
            najmniejszy_mianownik = lista[i][1]
        if lista[i][0] / lista[i][1] == najmniejsza_liczba:
            if lista[i][1] < najmniejszy_mianownik:
                najmniejszy_mianownik = lista[i][1]
                najmniejszy_ulamek = [int(najmniejszy_mianownik * najmniejsza_liczba), najmniejszy_mianownik]
    print(najmniejszy_ulamek)

def b():
    ile = 0
    for i in lista:
        if not czy_skracalny(i):
            ile += 1
    print(ile)

def c():
    suma = 0
    for i in lista:
        suma += skrocenie_ulamka(i)[0]
    print(suma)

def d():
    suma = 0
    b = 2*2*3*3*5*5*7*7*13
    for i in lista:
        suma += (i[0] * b) / i[1]
    print(suma)

d()