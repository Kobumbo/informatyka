a = int(input('Podaj liczbe a: '))
b = int(input('Podaj liczbe b: '))

for i in range(a, b + 1):
    for j in range(a, b + 1):
        for k in range(a, b + 1):
            if i ** 2 + j ** 2 == k ** 2:
                print(f'a = {i}, b == {j}, c = {k}')
