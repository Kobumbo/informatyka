# s = [2, 3, 1, 6, 4, 3, 7]
# i = 0
# temp = 0
# while i < len(s)-1:
#     if s[i] > s[i+1]:
#         temp = s[i+1]
#         s[i+1] = s[i]
#         s[i] = temp
#     i += 1
# print(s[len(s)-1])

# for n in range(3000,4000):
#     x= n
#     nk = n
#     w = 0
#     while n > 0:
#         w = n%10 + w
#         # print(f'w{w}')
#         n = n//10
#         # print(f'n{n}')
#     l = 0
#     while nk > n:
#         l = l + 1
#         # print(f'l{l}')
#         nk = nk//10
#         # print(f'nk{nk}')
#     if l-w ==0:
#         print(x, l-w)
#
# suma = 0
# n = 1340
# while n>0:
#     if (n%10)%2 == 1:
#         suma = suma + (n%10)
#     n = n//10
# print(suma)



x = 'tekst'
def rek(p, k):
    tekst = list(x)
    if p >= k:
        return
    s = (p+k)//2
    a = tekst[p-1]
    tekst[p-1] = tekst[k-1]
    tekst[k-1] = a
    rek(p,s)
    rek(s+1,k)
    return tekst

print(rek(1,5))










p = 1 k = 6

