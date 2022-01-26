import math

n = int(input('Podaj liczbe: '))
def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(math.sqrt(liczba))+1, 1):
        if liczba % i == 0:
            return False
    return True

print(czy_pierwsza(n))