import string


ANSWER = 871198282


def alphabetical_value(name):
    return sum(string.ascii_uppercase.index(letter) + 1 for letter in name)


def main():
    lst = sorted(open('../txt/problem022.txt').readline()[1:-1].split('","'))
    return sum((i + 1) * alphabetical_value(name) for i, name in enumerate(lst))


if __name__ == '__main__':
    print(main())
