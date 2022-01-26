while True:
    try:
        h = int(input('Podaj ilosc liczb: '))
        for i in range(h):
            print(3*i, end=', ')
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')