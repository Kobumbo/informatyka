n = int(input('Podaj liczbe n: '))
lista = []

for i in range(2, n+1):
    lista.append(i)

for i in range(len(lista)):
    if lista[i] != 0:
        print(lista[i])
        for j in range(i+1, len(lista)):
            if lista[j] % lista[i] == 0:
                lista[j] = 0

