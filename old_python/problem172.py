import array

def fact (n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

fact = [fact(i) for i in range(20)]

def C (n, k):
    return fact[n]//fact[n-k]//fact[k]

def perestanovki (lst, s): # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = C(s-1, lst[0])
    s -= lst[0]
    for i in range(1, 10):
        result *= C(s, lst[i])
        s -= lst[i]
    return result


lst = [array.array('L', (0 for i in range(10))) for j in range(10)]
for i in range(10):
    lst[i][i] = 1

#for k in lst:
#    print(k, perestanovki(k, 1))

result = 0
for i in range (2, 27):
    print(i, len(lst))
    newar = []
    for k in lst:
        ind = 0
        for j in range(9, -1, -1):
            if k[j] != 0:
                ind = j
                break
        for j in range(ind, 10):
            if k[j] < 3:
                newar.append(k[:])
                newar[-1][j] += 1
    lst = newar

for k in lst:
    result += perestanovki(k, 18)
print(result)
print(len(lst))
