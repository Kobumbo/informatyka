ciag = input('Podaj liczby oddzielone spacja: ')
lista = ciag.split()
minimum = int(lista[0])
ile_razy = 0
for i in range(len(lista)):
    liczba = int(lista[i])
    if minimum > liczba:
        minimum = liczba
        ile_razy = 0
    if liczba == minimum:
        ile_razy += 1
print(minimum)
print(ile_razy)

      