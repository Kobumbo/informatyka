wiadomosci = [i.strip() for i in open('wiadomosci.txt', 'r')]
podpisy = [i.strip() for i in open('podpisy.txt', 'r')]

def skrot(wiadomosc):
    wiadomosc = list(wiadomosc)
    S = []
    for i in 'ALGORYTM':
        S.append(ord(i))
    for i in range(8,len(wiadomosc), 9):
        wiadomosc.insert(i, '.')
    wiadomosc = ''.join(wiadomosc)
    wiadomosc = wiadomosc.split('.')

skrot('ajfbnghnhkhrthrhjrjjdfsssssssssssskjhkjghadsjgsjkgskghjgjgkashkjgsjgsjkhgjasgs')