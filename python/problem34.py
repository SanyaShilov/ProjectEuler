import euler


ANSWER = 40730


def main():
    total = 0
    for i in range(10, 2177280):
        if i == sum(euler.factorials[int(digit)] for digit in str(i)):
            total += i
    return total


if __name__ == '__main__':
    print(main())
