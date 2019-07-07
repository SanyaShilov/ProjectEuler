import euler
power = 50
LIMIT = 2**power
prime_list = euler.prime_list(2**(power//2))
squares = [p*p for p in prime_list]

print('done')

def foo (num, ind):
    result = num
    for i in range(ind):
        r = num//squares[i]
        if not r:
            break
        result -= foo(r, i)
    return result

print(foo(2**power, len(prime_list)))
