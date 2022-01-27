ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()
minimum = int(lista[0])
for i in range(len(lista)):
    liczba = int(lista[i])
    if minimum > liczba:
        minimum = liczba
print(minimum)
