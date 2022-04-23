szyfr1 = [i.strip() for i in open('szyfr1.txt', 'r')]
szyfr2 = [i.strip() for i in open('szyfr2.txt', 'r')]
szyfr3 = [i.strip() for i in open('szyfr3.txt', 'r')]

def a():
    klucz = szyfr1[6].split()
    for i in range(len(szyfr1) - 1):
        szyfr1[i] = list(szyfr1[i])
        for j in range(len(szyfr1[i])):
            szyfr1[i][j], szyfr1[i][int(klucz[j % 50]) - 1] = szyfr1[i][int(klucz[j % 50]) - 1], szyfr1[i][j]
        print(''.join(szyfr1[i]))

def b():
    klucz = szyfr2[1].split()
    for i in range(len(szyfr2) - 1):
        szyfr2[i] = list(szyfr2[i])
        for j in range(len(szyfr2[i])):
            szyfr2[i][j], szyfr2[i][int(klucz[j % 15]) - 1] = szyfr2[i][int(klucz[j % 15]) - 1], szyfr2[i][j]
        print(''.join(szyfr2[i]))

def c():
    klucz = szyfr3[1].split()
    for i in range(len(klucz)):
        klucz[i] = int(klucz[i])
    szyfr3[0] = list(szyfr3[0])
    for i in range(len(szyfr3[0]) - 1, -1, -1):
        szyfr3[0][i], szyfr3[0][klucz[i % len(klucz)] - 1] = szyfr3[0][klucz[i % len(klucz)] - 1], szyfr3[0][i]
    print(''.join(szyfr3[0]))

c()

