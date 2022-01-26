ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()

def suma_cyfr(cyfra):
    suma = 0
    for i in range(len(cyfra)):
        suma += int(cyfra[i])
    return suma

for i in lista:
    if suma_cyfr(i) == 10:
        print(i)