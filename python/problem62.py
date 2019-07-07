ANSWER =


def numbers (n):
    s = str(n)
    lst = [0 for i in range(10)]
    for i in range(10):
        lst[i] = s.count(str(i))
    return lst

lst = [numbers(i**3) for i in range(10000)]
for i in range(10000):
    if lst.count(lst[i]) == 5:
        print(i**3)
        break


if __name__ == '__main__':
    print(main())
