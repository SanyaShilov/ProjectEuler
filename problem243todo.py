#
# количество чисел меньших н, не имеющих с ним общих делителей
import euler

ar = [i for i in range(1000000)]
for i in range(2, 1000) :
    for j in range(2, 1000000//i+100) :
        try :
            ar[i*j] = 0
        except :
            pass
ar[1] = 0
pr = [i for i in ar if i != 0]

def abc (n) :
    c = n
    for k in pr :
        if k > n :
            break
        if n % k == 0 :
            c -= c//k
    return c
def res (n) :
    return abc(n) / (n-1)
'''
s = 0
for i in range(2, 1000001) :
    print(i)
    s += abc(i)
print(s)
'''
print(abc(510510))
print(15499/94744)
print(res(2*3*5*7*11*13*17))
print(2*3*5*7*11*13*17)
