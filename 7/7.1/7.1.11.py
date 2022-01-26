while True:
    try:
        y = int(input('Podaj wysokosc trojkata: '))
        for i in range(y):
            for j in range(y):
                if j+1>=y-i:
                    print('X',end='')
                else:
                    print(' ',end='')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')

# j 01234  i    y 5
#   ----X  0
#   ---XX  1
#   --XXX  2
#   -XXXX  3
#   XXXXX  4

