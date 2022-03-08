from re import L


plik = open('binarne.txt', 'r')

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

def a():
    ile = 0
    maksymalna_dlugosc = 0
    for i in lista:
        if i[0:int(len(i)/2)] == i[int(len(i)/2):]:
            ile += 1
            if len(i) > maksymalna_dlugosc:
                maksymalna_dlugosc = len(i)
                napis = i
    print(ile)
    print(maksymalna_dlugosc)
    print(napis)

def b():
    ile = 0
    lista_dlugosci = []
    for i in lista:
        for j in range(0,len(i), 4):
            if int(i[j:j+4], 2) > 9:
                ile += 1
                lista_dlugosci.append(len(i))
                break
    print(ile)
    print(min(lista_dlugosci))

def c():
    lista_liczb = []
    for i in lista:
        if int(i, 2) <= 65535:
            lista_liczb.append(int(i,2))
    print(max(lista_liczb))
    print(bin(max(lista_liczb))[2:])
