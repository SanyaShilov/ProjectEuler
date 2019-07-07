import array


sqrt_LIMIT = 10**16


factorials = [1]
for _ in range(1, 1001):
    factorials.append(factorials[-1] * _)


def int_sqrt(n):
    if n < sqrt_LIMIT:
        return int(n ** 0.5)
    sqrt = 1
    sqr = 1
    while sqr <= n:
        sqrt <<= 1
        sqr <<= 2
    sqrt >>= 1
    sqr >>= 2
    temp = sqrt >> 1
    while temp:
        temp_sqrt = sqr + temp * ((sqrt << 1) + temp)
        if temp_sqrt <= n:
            sqrt += temp
            sqr = temp_sqrt
        temp >>= 1
    return sqrt


def count_divisors(n):
    d = 0
    sqrt = int_sqrt(n)   
    for i in range(1, sqrt + 1):
        if n % i == 0:
            d += 2
    if n == sqrt * sqrt:
        d -= 1
    return d


def sum_divisors(n):
    d = 1
    sqrt = int_sqrt(n)   
    for i in range(2, sqrt + 1):
        if n % i == 0:
            d += i + n // i
    if n == sqrt*sqrt:
        d -= sqrt
    return d


def is_prime(n, prime_list):
    sq = int(n ** 0.5)
    for pr in prime_list:
        if pr > sq:
            return True
        if not n % pr:
            return False


def prime_list_with_zeros(n):
    index = array.array('L', (range(n)))
    index[1] = 0
    for i in range(n):
        if index[i]:
            for j in range(2 * i, n, i):
                index[j] = 0
    return index


def prime_list(n):
    return array.array('L', (i for i in prime_list_with_zeros(n) if i))


def totientlist(n):
    result = array.array('L', (i for i in range(n)))
    for i in range(2, n):
        if result[i] == i:
            for j in range(i, n, i):
                result[j] -= result[j] // i
    return result


def gcd1(a, b):
    if a == 1:
        return True
    if not a:
        return False
    if a > b:
        return gcd1(a % b, b)
    return gcd1(b % a, a)


def pythagorean_trio(a):
    a2 = a * a
    for b in range(1, a):
        b2 = b * b
        yield a2 - b2, 2 * a * b, a2 + b2


def pythagorean_unique_trio(a):
    a2 = a * a
    for b in range(1, a):
        b2 = b * b
        x = a2 - b2
        y = 2 * a * b
        if gcd1(x, y):
            yield x, y, a2 + b2


def parsefraction(lst):
    b = 1
    a = lst[-1]
    for i in range(len(lst) - 1):
            c = a
            a = a * lst[-2 - i] + b
            b = c
    return a, b


def squarefraction(nn, leng):
    sq = nn ** 0.5
    tr = int(sq)
    add = -tr
    d = 1
    l = 0
    lst = []
    while True:
        lst.append(tr)
        l += 1
        wtf = nn - add * add
        d = wtf // d
        tr = int((sq - add) / d)
        add = -add - tr * d
        if l > leng:
            break
    return lst


def notdivisible(num, lst, ind):
    # ind = len(lst)
    result = num
    for i in range(ind):
        r = num // lst[i]
        if not r:
            break
        result -= notdivisible(r, lst, i)
    return result


def pandigital(n):
    lst = [False for _ in range(10)]
    while n:
        r = n % 10
        if lst[r]:
            return False
        lst[r] = True
        n //= 10
    return True


def list_of_prime_factors(n):
    factors = []
    pr = 2
    while pr <= n:
        if not n % pr:
            factors.append(pr)
            n //= pr
            pr -= 1
        pr += 1
    return factors


if __name__ == '__main__':
    print(list_of_prime_factors(600851475143))
