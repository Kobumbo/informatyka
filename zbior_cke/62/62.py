lista1 = [i.strip() for i in open('liczby1.txt', 'r')]
lista2 = [i.strip() for i in open('liczby2.txt', 'r')]

def a():
    print(min(lista1))
    print(max(lista1))
