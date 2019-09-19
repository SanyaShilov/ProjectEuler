ANSWER = None
SQUARES = [1, 3, 6, 8, 10, 11]  # [i ** 2 for i in range(1, 101)]


def count_sets(n, count, index):
    if n == 0:
        if count == 0:
            return 1
        return 0
    if count == 0:
        return 0
    if index < 0:
        return 0
    with_number = count_sets(n - SQUARES[index], count - 1, index - 1)
    if with_number > 1:
        return 2
    return with_number + count_sets(n, count, index - 1)


def main():
    length = len(SQUARES)
    minimum = sum(SQUARES[:length // 2])
    maximum = sum(SQUARES[length // 2:])
    total = 0
    for n in range(minimum, maximum + 1):
        if count_sets(n, length // 2, length - 1) == 1:
            total += n
    return total


if __name__ == '__main__':
    print(main())
