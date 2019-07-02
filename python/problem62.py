ANSWER =


def numbers (n):
    s = str(n)
    ar = [0 for i in range(10)]
    for i in range(10):
        ar[i] = s.count(str(i))
    return ar

ar = [numbers(i**3) for i in range(10000)]
for i in range(10000):
    if ar.count(ar[i]) == 5:
        print(i**3)
        break


if __name__ == '__main__':
    print(main())
