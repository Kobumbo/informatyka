a = int(input('Podaj a:'))
b = int(input('Podaj b:'))
def nwd(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def nww(a,b):
    print(a*b//nwd(a,b))

nww(a,b)