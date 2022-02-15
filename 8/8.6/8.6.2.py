n = int(input('Podaj liczbe n: '))
a = 0
b = 1
c = 0
print(a)
print(b)
for i in range(n+1):
    c = a + b
    print(c)
    a = b
    b = c
