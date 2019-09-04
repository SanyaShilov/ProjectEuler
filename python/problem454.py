import euler


ANSWER = 9350130049860600
PRIME_LIST = euler.prime_list(165)
LIMIT = 1000


def number(lst):
    result = 1
    for i, power in enumerate(lst):
        result *= PRIME_LIST[i] ** power
    return result


def new_arrays(lst):
    for i in range(len(lst)):
        yield lst[:i] + (lst[i] + 1,) + lst[i + 1:]


def main():
    lst = tuple(0 for _ in range(len(PRIME_LIST)))
    ars = {lst}
    count = 0
    while ars:
        new_ars = set()
        for lst in ars:
            n = number(lst)
            if n >= LIMIT:
                continue
            n2 = n * n
            low_divisors = euler.low_divisors(n2)
            for i in low_divisors:
                j = n2 // i
                if i != j and n + j <= LIMIT:
                    count += 1
            new_ars.update(new_arrays(lst))
        ars = new_ars
    return count


if __name__ == '__main__':
    print(main())
