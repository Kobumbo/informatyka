while True:
    try:
        h = int(input('Podaj wysokosc: '))
        for i in range(h):
            for j in range(i+1):
                print((i+1)*(j+1), end=' ')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')