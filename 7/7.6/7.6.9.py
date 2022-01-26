import math

liczba = input('Podaj liczbe: ')
if math.sqrt(int(liczba)) == int(liczba) % 10:
    print('tak')
else:
    print('nie')
