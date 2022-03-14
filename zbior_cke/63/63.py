lista = [i.strip() for i in open('ciagi.txt', 'r')]

def a():
    for i in lista:
        if len(i) % 2 == 0:
            if i[:len(i)//2] == i[len(i)//2:]:
                print(i)

def b():
    ile = 0
    for i in lista:
        czy_obok = False
        for j in range(len(i)-1):
            if i[j] == i[j+1] == '1':
                czy_obok = True
        if not czy_obok:
            ile += 1
    print(ile)

