x = int(input('Podaj liczbe x: '))
n = int(input('Podaj potęgę liczby x: '))

liczba = 1
for i in range(1, n+1):
    liczba *= x
print(liczba)
