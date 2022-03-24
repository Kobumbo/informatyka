lista = [i.split() for i in open('dane_napisy.txt', 'r')]

def czy_anagram(lista):
    if len(lista[0]) != len(lista[1]):
        return False
    else:
        lista[0] = sorted(lista[0])
        lista[1] = sorted(lista[1])
    if lista[0] == lista[1]:
        return True
    return False

def a():
    ile = 0
    for i in lista:
        if i[0].count(i[0][0]) == len(i[0]) and i[1].count(i[1][0]) == len(i[1]) and czy_anagram(i):
            ile += 1
    print(ile)

def b():
    ile = 0
    for i in lista:
        if czy_anagram(i):
            ile += 1
    print(ile)

def c():
    lista2 = []
    ilosc_anagramow = []
    for i in lista:
        for j in i:
            lista2.append(j)
    for i in lista2:
        ile = 0
        for j in lista2:
            if czy_anagram([i, j]):
                ile += 1
        ilosc_anagramow.append(ile)
    print(max(ilosc_anagramow))



