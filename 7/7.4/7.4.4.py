n = int(input('Podaj n: '))

suma = 0
licznik = 0
liczba = 1

while licznik < n:
    if liczba % 7 == 0:
        suma += liczba
        licznik += 1
    liczba += 1
print(suma)