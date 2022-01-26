def suma_cyfr(cyfra):
    suma = 0
    for i in range(len(str(cyfra))):
        suma += int(str(cyfra)[i])
    return suma

n = int(input("Wpisz liczbę: "))

while len(str(n)) > 1:
    n = suma_cyfr(n)

print(n)