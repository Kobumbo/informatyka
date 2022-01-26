while True:
    try:
        y = int(input('Podaj wysokosc trojkata: '))
        for i in range(y):
            for j in range(i+1):
                print("X", end='')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')