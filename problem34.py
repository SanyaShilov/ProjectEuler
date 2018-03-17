fact = [1]
for i in range(1, 10) :
    fact.append(fact[-1]*i)

s = 0
for i in range(10, 2000000) :
    if i == sum(fact[int(k)] for k in str(i)) :
        s += i
print(s)
