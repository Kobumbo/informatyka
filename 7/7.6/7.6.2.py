liczba = int(input('Podaj liczbe: '))
def suma_cyfr(cyfra):
    suma = 0
    for i in range(len(cyfra)):
        suma += int(cyfra[i])
    return suma

print(suma_cyfr(liczba))