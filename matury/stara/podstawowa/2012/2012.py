plik = open("cyfry.txt", "r")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

def czy_rosnaca(wyraz):
    for i in range(len(wyraz) - 1):
        if wyraz[i] >= wyraz[i+1]:
            return False
    return True

def c():
    for wyraz in lista:
        if czy_rosnaca(wyraz):
            print(wyraz)
c()