import array

limit = 64000000

ar = array.array('Q', (1 for i in range(limit)))

print('done')
ar[0] = 0
for i in range(2, limit) :
    sq = i*i
    for j in range(i, limit, i) :
        ar[j] += sq
print('done')
s = 0
for i in range(limit) :
    n = ar[i]
    sq = n**0.5
    if sq == int(sq) :
        #print(i, n)
        s += i
print(s)
