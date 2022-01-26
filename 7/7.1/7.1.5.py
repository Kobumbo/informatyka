while True:
    try:
        wysokosc = int(input('Podaj wysokosc litery: '))
        grubosc = int(input('Podaj grubosc litery: '))
        szerokosc = int(input('Podaj szerokosc litery: '))
        for i in range(wysokosc-grubosc):
            for j in range(grubosc):
                print('L',end='')
            print()
        for k in range(grubosc):
            for l in range(szerokosc):
                print('L',end='')
            print()
        break
    except:
        print('Podaj poprawne dane! (Liczby calkowite)')

