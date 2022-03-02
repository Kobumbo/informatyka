plik = open("cyfry.txt", "r")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

def czy_rosnaca(wyraz):
    for i in range(len(wyraz) - 1):
        if wyraz[i] >= wyraz[i+1]:
            return False
    return True

def suma_cyfr(cyfra):
    suma = 0
    for i in range(len(cyfra)):
        suma += int(cyfra[i])
    return suma

def a():
    ile_parzystych = 0
    for wyraz in range(len(lista)):
        if wyraz % 2 == 0:
            ile_parzystych += 1
    print(ile_parzystych)

def b():
    lista_sum = []
    for wyraz in lista:
        lista_sum.append(suma_cyfr(wyraz))
    print(lista[lista_sum.index(max(lista_sum))])
    print(lista[lista_sum.index(min(lista_sum))])

def c():
    for wyraz in lista:
        if czy_rosnaca(wyraz):
            print(wyraz)


b()