import math

def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(math.sqrt(liczba))+1, 1):
        if liczba % i == 0:
            return False
    return True

n = int(input('Podaj n: '))
licznik = 0
suma = 0
liczba = 0
while licznik < n:
    if czy_pierwsza(liczba):
        suma += liczba
        licznik += 1
    liczba += 1
print(suma)