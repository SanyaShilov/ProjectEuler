import array
import functools
import math
import operator
import string


SQRT_LIMIT = 10 ** 16


FACTORIALS = [1]
for _ in range(1, 1001):
    FACTORIALS.append(FACTORIALS[-1] * _)


# divisors


def count_divisors(n):
    d = 0
    sqrt = int_sqrt(n)
    for i in range(1, sqrt + 1):
        if n % i == 0:
            d += 2
    if n == sqrt * sqrt:
        d -= 1
    return d


def count_prime_divisors(n, prime_lst=None):
    count = 0
    sqrt = int_sqrt(n) + 1
    prime_lst = prime_lst or [i for i in range(sqrt)]
    i = 0
    prime = prime_lst[i]
    while prime < sqrt:
        if not n % prime:
            count += 1
            while not n % prime:
                n //= prime
            sqrt = int_sqrt(n) + 1
        i += 1
        prime = prime_lst[i]
    if n > 1:
        count += 1
    return count


def sum_divisors(n):
    d = 1
    sqrt = int_sqrt(n)
    for i in range(2, sqrt + 1):
        if n % i == 0:
            d += i + n // i
    if n == sqrt * sqrt:
        d -= sqrt
    return d


def gcd1(a, b):
    return math.gcd(a, b) == 1


def is_not_divisible(num, lst, ind):
    # ind = len(lst)
    result = num
    for i in range(ind):
        r = num // lst[i]
        if not r:
            break
        result -= is_not_divisible(r, lst, i)
    return result


# primes


def is_prime(n, prime_lst, prime_lst_with_zeros=None):
    if prime_lst_with_zeros:
        try:
            return bool(prime_lst_with_zeros[n])
        except IndexError:
            pass
    sq = int(n ** 0.5)
    for prime in prime_lst:
        if prime > sq:
            return True
        if not n % prime:
            return False
    raise RuntimeError('Cannot determine if {} is prime'.format(n))


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


def list_of_prime_factors(n):
    factors = []
    prime = 2
    while prime <= n:
        if not n % prime:
            factors.append(prime)
            n //= prime
            prime -= 1
        prime += 1
    return factors


# pythagorean


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


# special numbers


def is_palindrome(num):
    str_n = str(num)
    return str_n == str_n[::-1]


def is_pandigital(n):
    str_n = str(n)
    return len(str_n) == len(set(str_n))


def is_pandigital_1n(n):
    str_n = str(n)
    return len(str_n) == len(set(str_n)) == int(max(str_n))


def triangular(n):
    return n * (n + 1) // 2


def pentagonal(n):
    return n * (3 * n - 1) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def is_pentagonal(n):
    a = (1 + (1 + 24 * n) ** 0.5) / 6
    return round(a) == round(a, 7)


# strings


def alphabetical_value(word):
    return sum(string.ascii_uppercase.index(letter) + 1 for letter in word)


# digits


def digit_sum(n):
    return sum(int(digit) for digit in str(n))


# other


def product(sequence, initial=1):
    return functools.reduce(operator.mul, sequence, initial)


def int_sqrt(n):
    if n < SQRT_LIMIT:
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


def totient_list(n):
    result = array.array('L', (i for i in range(n)))
    for i in range(2, n):
        if result[i] == i:
            for j in range(i, n, i):
                result[j] -= result[j] // i
    return result


def parse_fraction(lst):
    b = 1
    a = lst[-1]
    for i in range(len(lst) - 1):
        a, b = a * lst[-2 - i] + b, a
    return a, b


def square_fraction(n, length):
    sqrt = n ** 0.5
    a = int(sqrt)
    diff = -a
    denom = 1
    current_length = 0
    lst = []
    while True:
        lst.append(a)
        current_length += 1
        denom = (n - diff * diff) // denom
        a = int((sqrt - diff) / denom)
        diff = -diff - a * denom
        if current_length > length:
            break
    return lst


if __name__ == '__main__':
    print(square_fraction(23, 10))
