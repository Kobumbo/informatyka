lista = [i.split() for i in open('tekst.txt', 'r')]

def maksymalny_ciag_spolglosek(wyraz):
    dlugosc = 0
    maksymalna_dlugosc = 0
    samogloski = ['A', 'E', 'I', 'O', 'U', 'Y']
    for i in wyraz:
        if i not in samogloski:
            dlugosc += 1
            if dlugosc > maksymalna_dlugosc:
                maksymalna_dlugosc = dlugosc
        else:
            dlugosc = 0
    return maksymalna_dlugosc


# print(lista)
def a():
    ile = 0
    for i in lista[0]:
        for j in range(len(i) - 1):
            if i[j] == i[j + 1]:
                ile += 1
                break
    print(ile)

def b():
    lista_liter = [0]*26
    liczba_liter = 0
    for i in lista[0]:
        for j in range(len(i)):
            lista_liter[ord(i[j]) - 65] += 1
            liczba_liter += 1
    for i in range(len(lista_liter)):
        print(str(chr(65+i)) + ':', lista_liter[i], '(' + str(round(lista_liter[i]/liczba_liter * 100, 2)) + '%)')
        # print(lista_liter[i]/liczba_liter * 100)          #  (drukowanie wyniku do zaokraglenia) w odpowiedziach zle zaokraglone wyniki
    # print(liczba_liter)

def c():
    maksymalna_dlugosc_podslowa = []
    slowo = []
    for i in lista[0]:
        maksymalna_dlugosc_podslowa.append(maksymalny_ciag_spolglosek(i))
    maks = max(maksymalna_dlugosc_podslowa)
    ile = maksymalna_dlugosc_podslowa.count(maks)
    for i in lista[0]:
        if maksymalny_ciag_spolglosek(i) == maks:
            slowo.append(i)
    print(maks, ile, slowo[0])

