liczba = input('Podaj liczbe: ')
zmieniona = ''

for i in range(len(liczba)):
    zmieniona += str((int(liczba[i]) + int(liczba[i]) ** 2) % 10)

print(zmieniona)