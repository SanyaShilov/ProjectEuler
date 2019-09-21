import euler


PRIME_LIST = euler.prime_list(190)
LIMIT = euler.product(PRIME_LIST)
SQRT = euler.int_sqrt(LIMIT)


class Global:
    RESULT = 0


def work(number, product, index):
    for i in range(42 - 1, index, -1):
        new_product = product * PRIME_LIST[i]
        new_number = number - number % new_product
        if new_number > Global.RESULT:
            if not LIMIT % new_number:
                Global.RESULT = new_number
                print(Global.RESULT % 10 ** 16)
            work(new_number, new_product, i)


def main():
    work(SQRT, 1, -1)
    return Global.RESULT % 10 ** 16


if __name__ == '__main__':
    print(main())
