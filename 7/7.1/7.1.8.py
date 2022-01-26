while True:
    try:
        y = int(input('Podaj wysokosc trojkata: '))
        x = y * 2 - 1
        for i in range(y):
            for j in range(x+1):
                if j == (y-i) or j == (y+i) or i == (y-1) and j > (y-i) and j < (y+i):
                    print("X",end='')
                else:
                    print(" ",end='')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')