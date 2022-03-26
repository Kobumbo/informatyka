lista = [i.split() for i in open('napisy.txt', 'r')]

def wspolna_koncowka(lista):
    litera = []
    for i in range(len(lista[0])):
        if lista[0][::-1][i] != lista[1][::-1][i]:
            break
        litera.append(lista[0][::-1][i])
    return ''.join(litera[::-1])

def a():
    ile = 0
    lista_2 = []
    for i in lista:
        dl_1 = 0
        dl_2 = 0
        if len(i[0]) > len(i[1]):
            dl_1 = len(i[0])
            dl_2 = len(i[1])
        else:
            dl_1 = len(i[1])
            dl_2 = len(i[0])
        if dl_1 >= 3 * dl_2:
            ile += 1
            lista_2.append(i)
    print(ile)
    print(*lista_2[0])


def b():
    for i in lista:
        if i[0] == i[1][:len(i[0])]:
            print(*i, i[1][len(i[0]):])

def c():
    lista_dlugosci = []
    for i in lista:
        lista_dlugosci.append(len(wspolna_koncowka(i)))
    max_dlugosc = max(lista_dlugosci)
    for i in lista:
        if len(wspolna_koncowka(i)) == max_dlugosc:
            print(*i)
    print('Max dlugosc:', max_dlugosc)


