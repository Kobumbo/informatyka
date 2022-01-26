n = int(input('Podaj ilosc liczb: '))
licznik = 0
suma = 0
liczba = 1
while licznik < n:
    if liczba % 10 == 1 or liczba % 10 == 2 or liczba % 10 == 7:
        suma += liczba
        licznik += 1
    liczba += 1
print(suma)