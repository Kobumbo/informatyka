tekst = [i.split() for i in open('tekst.txt', 'r')]
probka = [i.split() for i in open('probka.txt', 'r')]


def szyfrowanie(slowo, klucz):
    lista = []
    for i in slowo:
        lista.append(i)
    for i in range(len(lista)):
        lista[i] = ord(lista[i]) - 97
        lista[i] = lista[i] * klucz[0] + klucz[1]
        if lista[i] > 25:
            lista[i] = lista[i] % 26
            lista[i] = chr(lista[i] + 97)
        else:
            lista[i] = chr(lista[i] + 97)
    return ''.join(lista)



def a():
    for i in tekst[0]:
        if i[0] == i[-1] == 'd':
            print(i)

def b():
    klucz = [5, 2]
    for i in tekst[0]:
        if len(i) >= 10:
            print(szyfrowanie(i, klucz))

def c():
    for p in probka:
        klucz_szyfrujacy = []
        klucz_deszyfrujacy = []
        for i in range(26):
            for j in range(26):
                klucz = [i, j]
                if szyfrowanie(p[0], klucz) == p[1]:
                    klucz_szyfrujacy = klucz
                if szyfrowanie(p[1], klucz) == p[0]:
                    klucz_deszyfrujacy = klucz
        print('Klucz szyfrujacy', klucz_szyfrujacy, 'Klucz deszyfrujacy', klucz_deszyfrujacy)