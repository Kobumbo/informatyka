lista1 = [i.strip() for i in open('liczby1.txt', 'r')]
lista2 = [i.strip() for i in open('liczby2.txt', 'r')]

def a():
    print(min(lista1))
    print(max(lista1))

def b(): #!!!!!!!!!!!
    pierwszy_wyraz = lista2[0]
    maksymalna_dlugosc = 0
    ile = 0
    for i in range(len(lista2)-1):
        if lista2[i] <= lista2[i+1]:
            ile += 1
            if ile > maksymalna_dlugosc:
                maksymalna_dlugosc = ile
        else:
            ile = 0
            pierwszy_wyraz = lista2[i+1]
    print(maksymalna_dlugosc)
    print(pierwszy_wyraz)

def c():
    ile_takich_samych = 0
    ile_pierwszy_wiekszy_od_drugiego = 0
    for i in range(len(lista1)):
        if int(lista1[i], 8) == int(lista2[i]):
            ile_takich_samych += 1
        if int(lista1[i], 8) > int(lista2[i]):
            ile_pierwszy_wiekszy_od_drugiego += 1
    print(ile_takich_samych)
    print(ile_pierwszy_wiekszy_od_drugiego)

def d():
    ile_razy_w_dziesietnym = 0
    ile_razy_w_osemkowym = 0
    lista2_na_osemkowy = []
    for i in lista2:
        ile_razy_w_dziesietnym += i.count('6')
    for i in lista2:
        lista2_na_osemkowy.append(oct(int(i))[2:])
    for i in lista2_na_osemkowy:
        ile_razy_w_osemkowym += i.count('6')
    print(ile_razy_w_osemkowym)
    print(ile_razy_w_dziesietnym)


