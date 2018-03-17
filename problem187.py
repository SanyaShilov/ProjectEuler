import array

n = 10**8

def big_list (n) :
    ar = array.array('L', (0 for i in range(n)))
    print('done')
    i = 2
    while i < n :
        if i % 10000 == 0 :
            print(i)
        if not ar[i] :
            power = i
            while power < n :
                temp = power
                while temp < n :
                    ar[temp] += 1
                    temp += power
                power *= i
        i += 1
    return ar

res = 0
lst = big_list(n)
for i in lst :
    if i == 2 :
        res += 1
print(res)
