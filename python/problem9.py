import euler


ANSWER = 31875000
SUM = 1000


def main():
    return euler.product(
        next(
            trio
            for a in range(int((SUM // 2) ** 0.5))
            for trio in euler.pythagorean_trio(a)
            if sum(trio) == SUM
        )
    )


if __name__ == '__main__':
    print(main())
