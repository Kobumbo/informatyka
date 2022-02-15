ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()

for i in lista:
    if 4 <= int(i) < 15:
        print(i)