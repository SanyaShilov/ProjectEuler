import euler


PRIME_LIST = euler.prime_list(10 ** 5)


def main():
    # число лежит между 0.00000000137 и 0.00000000138
    last = 0
    for i in range(100000):
        s = str(i * 56789)
        if s.endswith('99999'):
            last = i
    last_digit_sum = sum((9 * i) % 10 for i in range(10))
    results = []
    for i in range(
            int(round(1 / 0.00000000138, -5)) + last,
            int(round(1 / 0.00000000137, -5)),
            10 ** 5
    ):
        if euler.is_prime(i, PRIME_LIST):
            n = i - 1
            result = last_digit_sum * (n // 10)
            for j in range(n % 10):
                result += (9 * j) % 10
            results.append(result)
    return results


if __name__ == '__main__':
    print(main())
