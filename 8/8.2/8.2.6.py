ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()
minimum = int(lista[0])
minimum2 =  int(lista[0])
for i in range(len(lista)):
    liczba = int(lista[i])
    if minimum > liczba:
        minimum = minimum2
        minimum = liczba
    elif liczba < minimum2  or minimum2 == minimum:
        minimum2 = liczba
print(minimum2)