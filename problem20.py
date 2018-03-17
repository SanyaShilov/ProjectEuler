fact = [1]
for i in range(1, 101) :
    fact.append(fact[-1]*i)
print(sum(ord(c) for c in str(fact[100]))-ord('0')*len(str(fact[100])))
