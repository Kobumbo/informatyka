plik = open('liczby.txt', 'r')

def dzielniki(liczba):
    dzielniki = []
    for i in range(1, int(liczba/2) + 1):
        if liczba % i == 0:
            dzielniki.append(i)
    dzielniki.append(liczba)
    return dzielniki



def a():
    lista = [linia.strip() for linia in plik if int(linia) < 1000]
    print(len(lista))
    print(*lista[len(lista)-2:])

def b():
    lista = [linia.strip() for linia in plik if len(dzielniki(int(linia))) == 18]
    for i in lista:
        print(i)
        print(*dzielniki(int(i)))
        print()

b()
