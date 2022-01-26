liczba = input('Podaj liczbe: ')
zmieniona = ''

for i in range(len(liczba)):
    zmieniona += str(int(liczba[i]) ** 2)

print(zmieniona)