import math

import euler


ANSWER = 232792560
LIMIT = 20


def main():
    prime_list = euler.prime_list(LIMIT + 1)
    result = 1
    for prime in prime_list:
        result *= prime ** int(math.log(LIMIT, prime))
    return result


if __name__ == '__main__':
    print(main())
