import math
plik1 = open('dane_systemy1.txt', 'r')
plik2 = open('dane_systemy2.txt', 'r')
plik3 = open('dane_systemy3.txt', 'r')

lista1 = plik1.readlines()
lista2 = plik2.readlines()
lista3 = plik3.readlines()

for i in range(len(lista1)):
    lista1[i] = lista1[i].split()
    lista2[i] = lista2[i].split()
    lista3[i] = lista3[i].split()

def z_binarnego(liczba):
    return int(liczba, 2)

def z_czworkowego(liczba):
    return int(liczba, 4)

def z_osemkowego(liczba):
    return int(liczba, 8)


lista1_dziesietny_temperatury = []
lista2_dziesietny_temperatury = []
lista3_dziesietny_temperatury = []
for i in lista1:
    lista1_dziesietny_temperatury.append(z_binarnego(i[1]))
for i in lista2:
    lista2_dziesietny_temperatury.append(z_czworkowego(i[1]))
for i in lista3:
    lista3_dziesietny_temperatury.append(z_osemkowego(i[1]))


def a():   
    print(bin(min(lista1_dziesietny_temperatury)).replace('0b', ''))
    print(bin(min(lista2_dziesietny_temperatury)).replace('0b', ''))
    print(bin(min(lista3_dziesietny_temperatury)).replace('0b', ''))


def b():
    ile = 0
    for i in range(len(lista1)):
        if z_binarnego(lista1[i][0]) % 12 != 0 and z_czworkowego(lista2[i][0]) % 12 !=  0 and z_osemkowego(lista3[i][0]) % 12 != 0:
            ile += 1
    print(ile)

def c():
    ile = 1
    maksymalna1 = lista1_dziesietny_temperatury[0]
    maksymalna2 = lista2_dziesietny_temperatury[0]
    maksymalna3 = lista3_dziesietny_temperatury[0]
    for i in range(len(lista1_dziesietny_temperatury)):
        rekord = False
        if lista1_dziesietny_temperatury[i] > maksymalna1:
            maksymalna1 = lista1_dziesietny_temperatury[i]
            rekord = True
        if lista2_dziesietny_temperatury[i] > maksymalna2:
            maksymalna2 = lista2_dziesietny_temperatury[i]
            rekord = True
        if lista3_dziesietny_temperatury[i] > maksymalna3:
            maksymalna3 = lista3_dziesietny_temperatury[i]
            rekord = True
        if rekord:
            ile += 1
    print(ile)


def d():
    maksymalny_skok = 0
    for i in range(len(lista1_dziesietny_temperatury)):
        for j in range(i+1, len(lista1_dziesietny_temperatury)):
            r = (lista1_dziesietny_temperatury[i]-lista1_dziesietny_temperatury[j]) ** 2
            skok = math.ceil(r/abs(i-j))
            if skok > maksymalny_skok:
                maksymalny_skok = skok
    print(maksymalny_skok)

d()


