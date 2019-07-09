import euler


ANSWER = 70600674
NUMBERS = 4


def main():
    lst = [
        [int(item) for item in line.split()]
        for line in open('../txt/problem011.txt').readlines()
    ]
    length = len(lst)
    maximum = 0
    for i in range(length - NUMBERS + 1):
        for j in range(length - NUMBERS + 1):
            for start_i, start_j, di, dj in [
                    (0, 0, 0, 1),
                    (0, 0, 1, 0),
                    (0, 0, 1, 1),
                    (NUMBERS - 1, 0, -1, 1)
            ]:
                maximum = max(
                    maximum,
                    euler.product(
                        (
                            lst[i + start_i + di * n][j + start_j + dj * n]
                            for n in range(NUMBERS)
                        )
                    )
                )
    return maximum


if __name__ == '__main__':
    print(main())
