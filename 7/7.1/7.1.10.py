while True:
    try:
        y = int(input('Podaj wysokosc trojkata: '))
        for i in range(y):
            for j in range(i+1):
                if j == i or j == 0 or i == y-1:
                    print('X', end='')
                else:
                    print(' ', end='')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')