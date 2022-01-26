n = int(input('Ile liczb: '))

licznik = 0
suma = 0
liczba = 1
while licznik < n:
    while True:
        if str(liczba)[-2:] == '31' or str(liczba)[-2:] == '62' or str(liczba)[-2:] == '17':
            suma += liczba
            liczba += 1
            licznik += 1
            break
        else:
            liczba += 1
print(suma)