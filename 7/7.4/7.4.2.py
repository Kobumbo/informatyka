n = int(input('Podaj n: '))

liczba = 1
suma = 0
licznik = 0

while licznik < n:
    if liczba % 2 != 0:
        suma += liczba
        licznik += 1
    liczba += 1

print(suma)