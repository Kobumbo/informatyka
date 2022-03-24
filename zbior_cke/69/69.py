lista = [i.strip() for i in open('dane_geny.txt', 'r')]

def a():
    lista_gatunkow = [0] * 500
    for i in lista:
        lista_gatunkow[len(i)] += 1
    print(500-lista_gatunkow.count(0))
    print(max(lista_gatunkow))

def wydzielenie_genow(genotyp):
    geny = []
    gen = ''
    start = False
    koniec = False
    for i in range(len(genotyp) - 1):
        if genotyp[i] == 'A' and genotyp[i+1] == 'A':
            start = True
        if genotyp[i] == 'B' and genotyp[i+1] == 'B' and start:
            koniec = True
        if start and not koniec:
            gen += genotyp[i]
        if koniec:
            start = False
            koniec = False
            gen += 'BB'
            geny.append(gen)
            gen = ''
    return geny

def b():
    ile = 0
    for i in lista:
        geny = wydzielenie_genow(i)
        for j in geny:
            if 'BCDDC' in j:
                ile += 1
    print(ile)

def c():
    ilosc_genow = []
    wszystkie_geny = []
    for i in lista:
        ilosc_genow.append(len(wydzielenie_genow(i)))
        for j in wydzielenie_genow(i):
            wszystkie_geny.append(len(j))
    print('max ilosc genow', max(ilosc_genow))
    print('max dlugosc genu', max(wszystkie_geny))


# def d():
#     lista2 = lista
#     for i in range(len(lista2)):
#         lista2[i] = lista2[i][::-1]





