plik = open('dane_obrazki.txt', 'r')

lista = [linia.strip() for linia in plik]

obrazek = []
wszystkie_obrazki = []
for linia in lista:
    if len(linia) > 0:
        obrazek.append(linia)
    if len(obrazek) == 21:
        wszystkie_obrazki.append(obrazek)
        obrazek = []

def bit_parzystosci(tekst):
    if tekst.count('1') % 2 == 0:
        return 0
    return 1

def a():
    ile = 0
    max_czarnych = 0
    for i in wszystkie_obrazki:
        ile_czarnych = 0
        ile_bialych = 0
        for j in i[0:20]:
            ile_bialych += j[0:20].count('0')
            ile_czarnych += j[0:20].count('1')
        if ile_czarnych > ile_bialych:
            ile += 1
        if ile_czarnych > max_czarnych:
            max_czarnych = ile_czarnych
    print(f'{ile} rewersów')
    print(f'najwiecej czarnych pixeli - {max_czarnych}')


def b():
    ile = 0
    lista_obrazkow = []
    for i in wszystkie_obrazki:
        suma = 0
        for j in range(10):
            if i[j][0:10] == i[j][10:20] == i[j+10][0:10] == i[j+10][10:20]:
                suma += 1
        if suma == 10:
            lista_obrazkow.append(i)
            ile += 1
    print(ile)
    for i in range(20):
        print(lista_obrazkow[0][i][0:20])

def c():
    ile_poprawnych = 0
    ile_naprawialnych = 0
    ile_niepoprawnych = 0
    lista_bledow = []
    for i in wszystkie_obrazki:
        ile_niepoprawnych_wierszy = 0
        ile_niepoprawnych_kolumn = 0
        for j in i[:-1]:
            if bit_parzystosci(j[:-1]) != int(j[-1]):
                ile_niepoprawnych_wierszy += 1
        for j in range(20):
            tekst = ''
            for k in range(20):
                tekst += i[k][j]
            if bit_parzystosci(tekst) != int(i[-1][j]):
                ile_niepoprawnych_kolumn += 1
        lista_bledow.append(ile_niepoprawnych_kolumn + ile_niepoprawnych_wierszy)
        if ile_niepoprawnych_kolumn + ile_niepoprawnych_wierszy == 0:
            ile_poprawnych += 1
        elif ile_niepoprawnych_wierszy <= 1 and ile_niepoprawnych_kolumn <= 1:
            ile_naprawialnych += 1
        else:
            ile_niepoprawnych += 1
    print(f'{ile_poprawnych} - ilosc poprawnych')
    print(f'{ile_naprawialnych} - ilosc naprawialnych')
    print(f'{ile_niepoprawnych} - ilosc niepoprawnych')
    print(f'{max(lista_bledow)} - najwieksza liczba blednych bitow w jednym obrazku')

c()
