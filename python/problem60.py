import functools

import euler


ANSWER = 26033
COUNT = 5
COUNT1 = COUNT - 1
LIMIT = 10 ** 7
SLOW = True


PRIME_LIST_WITH_ZEROS = euler.prime_list_with_zeros(LIMIT)
PRIME_LIST = [n for n in PRIME_LIST_WITH_ZEROS if n]


@functools.lru_cache(maxsize=1000)
def check(a, b):
    if (
            euler.is_prime(int(a + b), PRIME_LIST, PRIME_LIST_WITH_ZEROS) and
            euler.is_prime(int(b + a), PRIME_LIST, PRIME_LIST_WITH_ZEROS)
    ):
        return True
    return False


def main():
    PRIME_LIST.remove(2)
    PRIME_LIST.remove(5)
    str_prime_list = [str(n) for n in PRIME_LIST]
    sets = {}
    minimum = LIMIT * COUNT
    for prime in str_prime_list:
        int_prime = int(prime)
        if int_prime >= minimum:
            break
        for lowest, rest in list(sets.items()):
            int_lowest = int(lowest)
            if int_lowest + int_prime >= minimum:
                sets.pop(lowest)
            elif check(prime, lowest):
                for lst in rest.copy():
                    if (
                            sum(int(n) for n in lst) + int_lowest + int_prime
                    ) >= minimum:
                        rest.remove(lst)
                    elif all(check(prime, n) for n in lst):
                        rest.append(lst.copy())
                        lst.append(prime)
                        if len(lst) == COUNT1:
                            minimum = min(
                                minimum, sum(int(n) for n in lst) + int_lowest
                            )
                            rest.remove(lst)
                rest.append([prime])
        if int_prime < minimum // COUNT:
            sets[prime] = []
    return minimum


if __name__ == '__main__':
    print(main())
