import math
ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()

for i in lista:
    if math.sqrt(lista.index(i)).is_integer():
        print(i)