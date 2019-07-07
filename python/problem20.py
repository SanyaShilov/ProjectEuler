import euler


ANSWER = 648
LIMIT = 100


def main():
    return sum(int(digit) for digit in str(euler.factorials[LIMIT]))


if __name__ == '__main__':
    print(main())
