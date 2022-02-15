ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()
minimum = int(lista[0])
minimum2 =  int(lista[0])
ile_razy = 0
for i in range(len(lista)):
    liczba = int(lista[i])
    if minimum > liczba:
        minimum2 = minimum
        minimum = liczba
    elif liczba < minimum2 or minimum2 == minimum:
        minimum2 = liczba
for liczba in lista:
    if int(liczba) == minimum2:
        ile_razy += 1
print(minimum2)
print(ile_razy)

