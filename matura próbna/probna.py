plik1 = open('robot.txt', 'r')
plik2 = open('plansza.txt', 'r')


lista1 = plik1.readlines()
lista2 = plik2.readlines()
for i in range(len(lista1)):
    lista1[i] = lista1[i].strip()
for i in range(len(lista2)):
    lista2[i] = lista2[i].split()

def a():
    ile = 0
    for i in lista1:
        wynik_gracza = 3
        x = 0
        y = 0
        for j in range(len(i)):
            if i[j] == 'N':
                y -= 1
            elif i[j] == 'E':
                x += 1
            elif i[j] == 'S':
                y += 1
            elif i[j] == 'W':
                x -= 1
            if x >= 0 and y >= 0:
                wynik_gracza += int(lista2[x][y])
            else:
                ile += 1
                break
    
    print(ile)    
    
                
def b():
    lista_punktow = []
    for i in lista1:
        wynik_gracza = 3
        x = 0
        y = 0
        for j in range(len(i)):
            if i[j] == 'N':
                y -= 1
            elif i[j] == 'E':
                x += 1
            elif i[j] == 'S':
                y += 1
            elif i[j] == 'W':
                x -= 1
            if x >= 0 and y >= 0:
                wynik_gracza += int(lista2[x][y])
            else:
                wynik_gracza = -1
                break
        lista_punktow.append(int(wynik_gracza))
    print(f'{max(lista_punktow)} - liczba punkow')
    print(f'{lista_punktow.index(max(lista_punktow)) + 1} - numer gracza') #co jezeli wiecej graczy ma tyle samo punktow - nie wypisuje ich

def dlugosc_serii(tekst):
        dlugosc = 0
        maksimum = 0
        for i in tekst:
            if i == 'W' or i == 'E':
                dlugosc += 1
                if dlugosc > maksimum:
                    maksimum = dlugosc
            else:
                dlugosc = 0
        return maksimum

def c():
    lista_dlugosci = []
    lista_numerow = []
    for i in lista1:
        lista_dlugosci.append(dlugosc_serii(i))
    for i in range(len(lista1)):
        x = lista1.index(lista1[i])
        if dlugosc_serii(lista1[i]) == max(lista_dlugosci):
            lista_numerow.append(lista1.index(lista1[i], x+i))
    print(lista_numerow)

lista_test = [15, 53, 15]

b()

