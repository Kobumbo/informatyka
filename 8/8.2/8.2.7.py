ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()
maksimum = int(lista[0])
maksimum2 =  int(lista[0])
ile_razy = 0
for i in range(len(lista)):
    liczba = int(lista[i])
    if maksimum < liczba:
        maksimum2 = maksimum
        maksimum = liczba
    elif liczba > maksimum2 or maksimum2 == maksimum:
        maksimum2 = liczba
for liczba in lista:
    if int(liczba) == maksimum2:
        ile_razy += 1
print(maksimum2)
print(ile_razy)

