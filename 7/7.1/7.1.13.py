while True:
    try:
        y = 2 * int(input('Podaj wysokosc krzyza: ')) + 1
        for i in range(y):
            for j in range(y):
                if j == y//2 or i == y//2:
                    print('#',end='')
                else:
                    print(' ',end='')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')