dane1 = [i.split() for i in open('dane1.txt', 'r')]
dane2 = [i.split() for i in open('dane2.txt', 'r')]
przyklad1 = [i.split() for i in open('przyklad1.txt', 'r')]
przyklad2 = [i.split() for i in open('przyklad2.txt', 'r')]

for i in range(len(dane1)):
    for j in range(len(dane1[i])):
        dane1[i][j] = int(dane1[i][j])
        dane2[i][j] = int(dane2[i][j])
for i in range(len(przyklad1)):
    for j in range(len(przyklad1[i])):
        przyklad1[i][j] = int(przyklad1[i][j])
        przyklad2[i][j] = int(przyklad2[i][j])


def a():
    ile = 0
    for i in range(len(dane1)):
        if dane1[i][9] == dane2[i][9]:
            ile += 1
    print(ile)

def b():
    ile = 0
    for i in range(len(dane1)):
        ile_parzystych_1 = 0
        ile_parzystych_2 = 0
        for j in range(10):
            if dane1[i][j] % 2 == 0:
                ile_parzystych_1 += 1
            if dane2[i][j] % 2 == 0:
                ile_parzystych_2 += 1
        if ile_parzystych_1 == ile_parzystych_2 == 5:
            ile += 1
    print(ile)

def c():
    ile = 0
    indeksy = []
    for i in range(len(dane1)):
        wypisz = False
        if set(dane1[i]) == set(dane2[i]):
            ile += 1
            wypisz = True
        if wypisz:
            indeksy.append(i+1)
    print('Ile', ile)
    print('Indeksy', *indeksy)

def d():
    for i in range(len(dane1)):
        ciag = []
        indeks_1 = 0
        indeks_2 = 0
        for j in range(20):
            if dane1[i][indeks_1] <= dane2[i][indeks_2]:
                ciag.append(dane1[i][indeks_1])
                indeks_1 += 1
            else:
                ciag.append(dane2[i][indeks_2])
                indeks_2 += 1
            if indeks_1 == 10:
                ciag1 = dane2[i][indeks_2:]
                ciag.extend(ciag1)
                break
            if indeks_2 == 10:
                ciag2 = dane1[i][indeks_1:]
                ciag.extend(ciag2)
                break
        print(*ciag)


