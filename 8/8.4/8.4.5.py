ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()

def czy_parzyste_cyfry(liczba):
    for i in str(liczba):
        if int(i) % 2 != 0:
            return False
    return True

for i in lista:
    if czy_parzyste_cyfry(i):
        print(i)