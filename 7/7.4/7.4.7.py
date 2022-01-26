def suma_cyfr(cyfra):
    suma = 0
    for i in range(len(cyfra)):
        suma += int(cyfra[i])
    return suma

n = int(input('Ile liczb: '))
licznik = 0
suma = 0
liczba = 0
while licznik < n:
    if suma_cyfr(str(liczba)) == 10:
        suma += liczba
        licznik += 1
    liczba += 1
print(suma)