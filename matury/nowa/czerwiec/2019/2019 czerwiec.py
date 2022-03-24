liczby = [i.strip() for i in open('liczby.txt', 'r')]
pierwsze = [i.strip() for i in open('pierwsze.txt', 'r')]

liczby_przyklad = [i.strip() for i in open('liczby_przyklad.txt', 'r')]
pierwsze_przyklad = [i.strip() for i in open('pierwsze_przyklad.txt', 'r')]

def czy_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

def suma_cyfr(liczba):
    suma = 0
    for i in liczba:
        suma += int(i)
    return str(suma)

def a():
    for i in liczby:
        if 5000 >= int(i) >= 100 and czy_pierwsza(int(i)):
            print(i)

def b():
    for i in pierwsze_przyklad:
        if czy_pierwsza(int(i[::-1])) and czy_pierwsza(int(i)):
            print(i)

def c():
    ile = 0
    for i in pierwsze:
        suma = suma_cyfr(i)
        while len(suma) > 1:
            suma = suma_cyfr(suma)
        if suma == '1':
            ile += 1
    print(ile)



