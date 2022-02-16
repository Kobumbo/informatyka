plik = open("hasla.txt", "r") #r - read, a - append, w - write


lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

def a():
    parzyste = 0
    for wyraz in lista:
        if len(wyraz) % 2 == 0:
            parzyste += 1
    print(a())
    print(len(lista) - a())

def b():
    for wyraz in lista:
        if wyraz == wyraz[::-1]:
            print(wyraz)

def c():
    for wyraz in lista:
        for i in range(len(wyraz)):
            if ord(wyraz[i-1]) + ord(wyraz[i]) == 220:
                print(wyraz)
                break
            