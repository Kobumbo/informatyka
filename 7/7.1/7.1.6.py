while True:
    try:
        height = int(input('Podaj wysokosc prostokata: '))
        width = int(input('Podaj szerokosc prostokata: '))
        for i in range(height):
            for j in range(width):
                print('X', end='')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')
