ANSWER = 4617456485273129588
LIMIT = 13082761331670030


def main():
    total = 0
    for i in range(153416670, LIMIT, 153416670):
        j = i + 1
        if j * j * j % LIMIT == 1:
            total += j
    return total


if __name__ == '__main__':
    print(main())
