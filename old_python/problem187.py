import array

n = 10**8

def big_list (n):
    lst = array.array('L', (0 for i in range(n)))
    print('done')
    i = 2
    while i < n:
        if i % 10000 == 0:
            print(i)
        if not lst[i]:
            power = i
            while power < n:
                temp = power
                while temp < n:
                    lst[temp] += 1
                    temp += power
                power *= i
        i += 1
    return lst

result = 0
lst = big_list(n)
for i in lst:
    if i == 2:
        result += 1
print(result)
