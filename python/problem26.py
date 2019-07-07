import euler


ANSWER = 983
LIMIT = 1000


def main():
    prime_list = euler.prime_list(LIMIT)
    prime_list.remove(2)
    prime_list.remove(5)
    maximum = 0
    val = 0
    ten = 10
    for prime in reversed(prime_list):
        if prime < maximum:
            break
        while ten < prime:
            ten *= 10
        temp = ten
        while True:
            if (temp - 1) % prime == 0:
                length = len(str((temp - 1) // prime))
                if length > maximum:
                    maximum = length
                    val = prime
                break
            temp *= 10
    return val


if __name__ == '__main__':
    print(main())
