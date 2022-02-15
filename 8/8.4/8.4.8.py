ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()

for i in lista:
    if int(i) < 0:
        i = 0
    print(i)