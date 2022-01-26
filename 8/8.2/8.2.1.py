ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()
maksimum = int(lista[0])
for i in range(len(lista)):
    liczba = int(lista[i])
    if maksimum < liczba:
        maksimum = liczba
print(maksimum)
