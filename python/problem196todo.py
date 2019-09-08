import functools

import euler


ANSWER = None
LIMIT = 10 ** 4
LIMIT2 = 5678027
PRIME_LIST = euler.prime_list(LIMIT + 100)


@functools.lru_cache()
def start_of_row(n):
    return n * (n - 1) // 2 + 1


@functools.lru_cache()
def number(n, i):
    if not 0 <= i < n:
        return 0
    return start_of_row(n) + i


@functools.lru_cache()
def is_prime(n, i):
    num = number(n, i)
    if not num:
        return False
    return euler.is_prime(num, PRIME_LIST)


@functools.lru_cache()
def primes_around(n, i):
    result = []
    for d_n in range(-1, 2):
        for d_i in range(-1, 2):
            if d_n or d_i:
                if is_prime(n + d_n, i + d_i):
                    result.append((n + d_n, i + d_i))
    return result


def calculate_row(n):
    result = 0
    for i in range(n):
        if is_prime(n, i):
            around = primes_around(n, i)
            if len(around) > 1:
                result += number(n, i)
            elif len(around) == 1:
                if len(primes_around(*around[0])) > 1:
                    result += number(n, i)
    return result


def main():
    return calculate_row(LIMIT)


if __name__ == '__main__':
    print(main())
