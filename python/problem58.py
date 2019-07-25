import euler


ANSWER = 26241


def main():
    lst = euler.prime_list(1000000)
    diff = 2
    primes = 3
    total = 5
    ratio = primes / total
    temp = 9
    while ratio >= 0.1:
        diff += 2
        for _ in range(3):
            temp += diff
            if euler.is_prime(temp, lst):
                primes += 1
        temp += diff
        total += 4
        ratio = primes / total
    return diff + 1


if __name__ == '__main__':
    print(main())
