import math

plik = open('liczby.txt', 'r')

lista = plik.readlines()

for i in range(len(lista)):
    lista[i] = lista[i].strip()



def iloczyn_cyfr(liczba):
    iloczyn = 1
    liczba = str(liczba)
    for i in liczba:
        iloczyn *= int(i)
    return iloczyn

def moc_liczby(liczba):
    moc = 1
    liczba = iloczyn_cyfr(liczba)
    while liczba > 9:
        liczba = iloczyn_cyfr(liczba)
        moc += 1
    return moc

def rozklad(liczba):
    czynniki = []
    x = 2
    if liczba % 2 == 0:
        return 0
    while liczba >= 2:
        while liczba % x == 0:
            liczba //= x
            if x not in czynniki:
                czynniki.append(x)
            if len(czynniki) > 3:
                return 0
        x += 1
    return len(czynniki)

# def rozklad(liczba):
#     czynniki = []
#     if liczba % 2 == 0:
#         return 0
#     for i in range(3, int(math.sqrt(liczba)) + 1, 2):
#         while liczba % i == 0:
#             liczba = liczba / i
#             if i not in czynniki:
#                 czynniki.append(i)
#             if len(czynniki) > 3:
#                 return 0
#     if liczba > 2:
#         czynniki.append(liczba)
#     return len(czynniki)

def a():
    ile = 0
    for i in lista:
        if rozklad(int(i)) == 3:
            ile += 1
    print(ile)



def b():
    ile = 0
    for i in lista:
        if str(int(i) + int(i[::-1])) == str(int(i) + int(i[::-1]))[::-1]:
            ile += 1
    print(ile)

def c():
    lista_mocy = []
    lista_mocy_1 = []
    for i in lista:
        lista_mocy.append(moc_liczby(i))
    for i in range(1,max(lista_mocy)+1):
        print(f'moc {i}: {lista_mocy.count(i)}')
    for i in lista:
        if moc_liczby(i) == 1:
            lista_mocy_1.append(int(i))
    print()
    print(f'maksymalna liczba o mocy 1: {max(lista_mocy_1)}')
    print(f'minimalna liczba o mocy 1: {min(lista_mocy_1)}')
            

a()
# b()
# c()

