while True:
    try:
        y = int(input('Podaj wysokosc wiezy: '))
        for i in range(y):
            for j in range(i+1):
                print('O', end='')
            print()
        break
    except:
        print('Podaj poprawna wartosc! (Liczba calkowita)')