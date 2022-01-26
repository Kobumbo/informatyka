#0   |-----A-----|
#1   |----A-A----|
#2   |---A---A---|
#3   |--AAAAAAA--|
#4   |-A-------A-|
#5   |A---------A|



while True:
    try:
        y = int(input('Podaj wysokosc litery: '))
        x = y * 2 - 1
        for i in range(y):
            for j in range(x+1):
                if j == (y - i) or j == (y + i) or i == y//2 and j > (y-i) and j < (y+i):
                    print('A', end='')
                else:
                    print(' ', end='')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')


