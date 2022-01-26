while True:
    try:
        a = int(input('Podaj bok kwadratu: '))
        for i in range(a):
            for j in range(a):
                print('K', end='')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')