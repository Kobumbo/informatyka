hasla = [i.strip() for i in open('hasla.txt', 'r')]

def a():
    ile = 0
    for i in hasla:
        try:
            i = int(i)
            ile += 1
        except:
            pass
    print(ile)

def b():
    lista_hasel = []
    for i in hasla:
        if hasla.count(i) >= 2:
            if i not in lista_hasel:
                lista_hasel.append(i)
    print(sorted(lista_hasel))

def c():    #???????
    pass

def d():
    ile = 0
    for i in hasla:
        numer = False
        mala = False
        duza = False
        for j in range(len(i)):
            if i[j].isnumeric():
                numer = True
            if i[j].islower():
                mala = True
            if i[j].isupper():
                duza = True
        if numer and mala and duza:
            ile += 1
    print(ile)