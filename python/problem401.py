res = 0
l = 1000000
rest = 10000
for i in range(1, l+1):
    res += (l//i)*i*i
print(res%rest)


# best code:

res = 0
for i in range(1, l+1):
    res += (l%i)*(i%rest)
print((-res)%rest)

'''
ten = 10
j = 1
for i in range(10**15):
    if i > ten:
        ten *= 10
        j += 1
        print(ten, j)
'''


def SumSquarsBeforeN (n):
    return n*(n+1)*(2*n+1)//6

def calc (n):
    res = 0
    for i in range(1, n+1):
        res += (n//i)*i*i
    return res

def newcalc (n):
    res = SumSquarsBeforeN(n)
    for i in range(1, n):
        res += (n//i)*i*i
    return res

def calcdel (n, d):
    res = 0
    for i in range():
        pass


if __name__ == '__main__':
    print(main())
