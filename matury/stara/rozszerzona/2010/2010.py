plik = open("anagram.txt", "r")
plik2 = open("odp_4a.txt", "w")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].split()
lista2 = lista.copy()

    
def taka_sama_liczba_znakow(wiersz):
    for i in range(len(wiersz)):
        if len(wiersz[i]) != len(wiersz[0]):
            return False
    return True

def kazdy_element_listy_jednakowy(lista):
    element = lista[0]
    for i in lista:
        if element != i:
            return False
    return True

def a():
    for i in lista:
        if taka_sama_liczba_znakow(i):
            for j in range(len(i)):
                print(i[j], end = ' ', file = plik2)
            print(file = plik2)
    plik2.close()


def b():
    for i in range(len(lista2)):
        if taka_sama_liczba_znakow(lista2[i]):
            for j in range(len(lista2[i])):
                lista2[i][j] = "".join(sorted(lista2[i][j]))
            if kazdy_element_listy_jednakowy(lista2[i]):
                print(lista[i])
b()
print(lista[0])
