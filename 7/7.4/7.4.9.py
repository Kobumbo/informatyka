def suma_cyfr(cyfra):
    suma = 0
    for i in range(len(cyfra)):
        suma += int(cyfra[i])
    return suma

def czy_pierwsza(cyfra):
    i = 2
    if cyfra < 2:
        return False
    while i < cyfra:
        if cyfra % i == 0:
            return False
        i += 1
    return True

n = int(input('Podaj n: '))
licznik = 0
suma = 0
liczba = 0
while licznik < n:
    if czy_pierwsza(suma_cyfr(str(liczba))) == True:
        suma += liczba
        licznik += 1
    liczba += 1
print(suma)