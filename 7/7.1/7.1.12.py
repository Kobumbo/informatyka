while True:
    try:
        y = int(input('Podaj wysokosc trojkata: '))
        for i in range(y):
            for j in range(y):
                if j+1 == y-i or j == y-1 or i == y-1:
                    print('X',end='')
                else:
                    print(' ',end='')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')