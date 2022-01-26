while True:
    try:
        h = int(input('Podaj wysokosc: '))
        for i in range(h):
            for j in range(i+1):
                print((2**(i+1))+j, end=',')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')