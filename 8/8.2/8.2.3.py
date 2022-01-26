ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()
maksimum = int(lista[0])
ile_razy = 0
for i in range(len(lista)):
    liczba = int(lista[i])
    if maksimum < liczba:
        maksimum = liczba
        ile_razy = 0
    if liczba == maksimum:
        ile_razy += 1
print(maksimum)
print(ile_razy)

