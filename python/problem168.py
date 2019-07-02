import primes



'''
prime_list = primes.prime_list(10000000)
print('done')
prime_list.remove(2)
prime_list.remove(5)

big = 10**100
s = 0
ten = 10
for pr in prime_list:
    while ten < pr:
        ten *= 10
    temp = ten
    while True:
        if (temp-1) % pr == 0:
            n = (temp-1) // pr
            if n > big:
                break
            r = int(str(n%10)+str(n//10))
            if r % n == 0:
                print(r, n)
                s += n
            break
        temp *= 10
'''

res = 0
for n in range(1, 10):
    print(n)
    N = 10*n - 1
    for f in range(1, 10):
        nf = n*f
        for power in range(1, 100):
            if (10**power * f - nf) % N == 0:
                num = ((10**power * f - nf)//N)*10 + f
                n2 = num*n
                if len(str(num)) == len(str(n2)):
                    res += num % 100000
print(res)


if __name__ == '__main__':
    print(main())
