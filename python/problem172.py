import array

def fact (n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

fact = [fact(i) for i in range(20)]

def C (n, k):
    return fact[n]//fact[n-k]//fact[k]

def perestanovki (ar, s): # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = C(s-1, ar[0])
    s -= ar[0]
    for i in range(1, 10):
        res *= C(s, ar[i])
        s -= ar[i]
    return res


ar = [array.array('L', (0 for i in range(10))) for j in range(10)]
for i in range(10):
    ar[i][i] = 1

#for k in ar:
#    print(k, perestanovki(k, 1))

res = 0
for i in range (2, 27):
    print(i, len(ar))
    newar = []
    for k in ar:
        ind = 0
        for j in range(9, -1, -1):
            if k[j] != 0:
                ind = j
                break
        for j in range(ind, 10):
            if k[j] < 3:
                newar.append(k[:])
                newar[-1][j] += 1
    ar = newar

for k in ar:
    res += perestanovki(k, 18)
print(res)
print(len(ar))


if __name__ == '__main__':
    print(main())
