import array

LIMIT = 64000000

lst = array.array('Q', (1 for i in range(LIMIT)))

print('done')
lst[0] = 0
for i in range(2, LIMIT):
    sq = i*i
    for j in range(i, LIMIT, i):
        lst[j] += sq
print('done')
s = 0
for i in range(LIMIT):
    n = lst[i]
    sq = n**0.5
    if sq == int(sq):
        #print(i, n)
        s += i
print(s)


if __name__ == '__main__':
    print(main())
