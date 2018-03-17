

fact = [1]
for i in range(1, 30) :
    fact.append(fact[-1]*i)

def comb (k, n) :
    if k > n :
        return 0
    return fact[n]//fact[k]//fact[n-k]




# часть решения
'''
sm = [0 for i in range(26+1)]
s = 0
for q in range(2, 26+1) :
    arstr = [[i] for i in range(q)]
    arlex = [0 for i in range(q)]
    arlen = [1 for i in range(q)]
    while arstr :
        st = arstr.pop()
        lex = arlex.pop()
        l = arlen.pop()
        if l == q :
            if lex :
                sm[l] += 1
            continue
        l1 = l+1
        if lex :
            for i in range(st[-1]) :
                if i not in st :
                    arstr.append(st[:]+[i])
                    arlen.append(l1)
                    arlex.append(1)
        else :
            for i in range(st[-1]) :
                if i not in st :
                    arstr.append(st[:]+[i])
                    arlen.append(l1)
                    arlex.append(0)
            for i in range(st[-1]+1, q) :
                if i not in st :
                    arstr.append(st[:]+[i])
                    arlen.append(l1)
                    arlex.append(1)
    print(q, sm[q], sm[q]*comb(q, 26))
print(max(sm))
'''

s = 0
for q in range(2, 26+1) :
    a = (2**q-q-1)*comb(q, 26)
    if a > s :
        s = a
print(s)
