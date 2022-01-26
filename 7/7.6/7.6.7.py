liczba = int(input('Podaj liczbe: '))
def czy_parzyste_cyfry(liczba):
    for i in str(liczba):
        if int(i) % 2 != 0:
            return False
    return True

print(czy_parzyste_cyfry(liczba))