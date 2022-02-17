plik = open("dane.txt", "r")

lista = plik.readlines()
for i in range(len(lista)):
    lista[i] = lista[i].strip()

def a():
    ilosc_mezczyzn = 0
    ilosc_kobiet = 0
    for i in lista:
        if int(i[9]) % 2 == 0:
            ilosc_kobiet += 1
        else:
            ilosc_mezczyzn += 1
    print(f'Ilosc kobiet: {ilosc_kobiet}')
    print(f'Ilosc mężczyzn: {ilosc_mezczyzn}')

def b():
    ilosc_osob = 0
    for i in lista:
        if i[2:4] == '11' or i[2:4] == '31':
            ilosc_osob += 1
    print(ilosc_osob)

def wzor_na_pesel(pesel):  
    mnozniki = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    suma = 0
    for i in range(len(pesel)):
        suma += int(pesel[i]) * mnozniki[i]
    return suma
    
def c():
    for i in lista:
        if wzor_na_pesel(i) % 10 != 0:
            print(i)