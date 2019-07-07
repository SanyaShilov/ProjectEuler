result = 0
l = 1000000
rest = 10000
for i in range(1, l+1):
    result += (l//i)*i*i
print(result%rest)


# best code:

result = 0
for i in range(1, l+1):
    result += (l%i)*(i%rest)
print((-result)%rest)

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
    result = 0
    for i in range(1, n+1):
        result += (n//i)*i*i
    return result

def newcalc (n):
    result = SumSquarsBeforeN(n)
    for i in range(1, n):
        result += (n//i)*i*i
    return result

def calcdel (n, d):
    result = 0
    for i in range():
        pass
