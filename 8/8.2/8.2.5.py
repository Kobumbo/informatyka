ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()
maksimum = int(lista[0])
maksimum2 =  int(lista[0])
for i in range(len(lista)):
    liczba = int(lista[i])
    if maksimum < liczba:
        maksimum = maksimum2
        maksimum = liczba
    elif liczba > maksimum2  or maksimum2 == maksimum:
        maksimum2 = liczba
print(maksimum)
print(maksimum2)