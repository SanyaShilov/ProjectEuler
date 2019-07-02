import array

LIMIT = 64000000

ar = array.array('Q', (1 for i in range(LIMIT)))

print('done')
ar[0] = 0
for i in range(2, LIMIT):
    sq = i*i
    for j in range(i, LIMIT, i):
        ar[j] += sq
print('done')
s = 0
for i in range(LIMIT):
    n = ar[i]
    sq = n**0.5
    if sq == int(sq):
        #print(i, n)
        s += i
print(s)
