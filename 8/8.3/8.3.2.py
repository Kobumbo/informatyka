ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()

for i in lista:
    print(float(i) ** 3)