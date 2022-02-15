ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()

for i in lista:
    if lista.index(i) % 2 == 0:
        print(i)