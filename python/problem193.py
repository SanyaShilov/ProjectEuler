import euler
power = 50
LIMIT = 2**power
prime_list = euler.prime_list(2**(power//2))
squares = [p*p for p in prime_list]

print('done')

def foo (num, ind):
    res = num
    for i in range(ind):
        r = num//squares[i]
        if not r:
            break
        res -= foo(r, i)
    return res

print(foo(2**power, len(prime_list)))


if __name__ == '__main__':
    print(main())
