import math

def czy_konczy_sie_pierwiastkiem(liczba):
    if math.sqrt(int(liczba)) != int(liczba) % 10:
        return False
    return True

a = int(input('Podaj liczbe a: '))
b = int(input('Podaj liczbe b: '))

for i in range(a, b + 1):
    if czy_konczy_sie_pierwiastkiem(i):
        print(i)