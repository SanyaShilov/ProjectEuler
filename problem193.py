import euler
power = 50
limit = 2**power
primelist = euler.primelist(2**(power//2))
squares = [p*p for p in primelist]

print('done')

def foo (num, ind) :
    res = num
    for i in range(ind) :
        r = num//squares[i]
        if not r :
            break
        res -= foo(r, i)
    return res

print(foo(2**power, len(primelist)))
