przyklad_plik = open('przyklad.txt', 'r')
plik = open('szyfry.txt', 'r')
przyklad_lista = przyklad_plik.readlines()
lista = plik.readlines()
jawne = [i.strip() for i in open('jawne.txt', 'r')]
przyklad_jawne = [i.strip() for i in open('przykladjawne.txt', 'r')]

for i in range(len(przyklad_lista)):
    przyklad_lista[i] = przyklad_lista[i].split()

for i in range(len(lista)):
    lista[i] = lista[i].split()

lista_szyfrogramow_przyklad = []
for i in range(len(przyklad_lista)):
    if len(przyklad_lista[i]) == 1:
        lista_szyfrogramow_przyklad.append(przyklad_lista[i + 1: i + 1 + int(przyklad_lista[i][0])])

lista_szyfrogramow = []
for i in range(len(lista)):
    if len(lista[i]) == 1:
        lista_szyfrogramow.append(lista[i + 1: i + 1 + int(lista[i][0])])

def zmiana_na_litery(x, y):
    return 65+x+5*y

def zamiana_na_liczby(tekst):
    wynik = []
    for i in tekst:
        if i == 'Z':
            wynik.append('')
        for j in range(5):
            for k in range(5):
                if chr(zmiana_na_litery(j, k)) == i:
                    wynik.append([j, k])
    return wynik

def przesuwanie_sie(lista):
    wynik = []
    x = int(lista[0][0])
    y = int(lista[0][1])
    wynik.append([x,y])
    for i in range(1, len(lista)):
        if x + int(lista[i][0]) < 5 and y + int(lista[i][1]) < 5:
            x += int(lista[i][0])
            y += int(lista[i][1])
            wynik.append([x,y])
        else:
            wynik.append('')
    return wynik

def szyfrowanie(tekst):
    i = 0
    wynik = []
    abc = zamiana_na_liczby(tekst)
    wynik.append([zamiana_na_liczby(tekst)[0][0],zamiana_na_liczby(tekst)[0][1]])
    for i in range(len(zamiana_na_liczby(tekst))-1):
        x1 = zamiana_na_liczby(tekst)[i+1][0] - zamiana_na_liczby(tekst)[i][0]
        y1 = zamiana_na_liczby(tekst)[i+1][1] - zamiana_na_liczby(tekst)[i][1]
        wynik.append([x1, y1])
    return wynik

slowa = []
for i in range(len(lista_szyfrogramow)):
    wynik = ''
    for j in przesuwanie_sie(lista_szyfrogramow[i]):
        try:
            wynik += chr(zmiana_na_litery(j[0], j[1]))
        except:
            wynik += 'Z'
    slowa.append(wynik)

def a():
    liczba_z = []
    for i in slowa:
        liczba_z.append(i.count('Z'))
    for i in slowa:
        if i.count('Z') == max(liczba_z):
            print(i)

def b():
    for i in slowa:
        if i == i[::-1]:
            print(i)

def c():
    for i in slowa:
        tekst = ''
        for j in i:
            if j not in tekst:
                tekst += j
        if len(tekst) <= 2:
            print(i)

def d():
    for i in jawne:
        ile = 0
        for j in szyfrowanie(i)[1:]:
            if j[0] == j[1]:
                ile += 1
        if ile != 0:
            print(i, ile)

# a()
# b()
# c()
# d()
