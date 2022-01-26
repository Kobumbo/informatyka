while True:
    try:
        x = int(input('Podaj szerokosc prostokata: '))
        y = int(input('Podaj wysokosc prostokata: '))
        for i in range(y):
            for j in range(x):
                if (i == 0 or i == y - 1) or (j == 0 or j == x - 1):
                    print('X', end='')
                else:
                    print(' ', end='')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')