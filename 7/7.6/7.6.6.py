a = int(input('Podaj a: '))
b = int(input('Podaj b: '))

for i in range(a, b + 1):
    if str(i) == str(i)[::-1]:
        print(i)