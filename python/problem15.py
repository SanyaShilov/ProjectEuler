import euler


ANSWER = 137846528820
GRID = 20, 20


def main():
    return (
        euler.factorials[GRID[0] + GRID[1]] //
        euler.factorials[GRID[0]] //
        euler.factorials[GRID[1]]
    )


if __name__ == '__main__':
    print(main())
