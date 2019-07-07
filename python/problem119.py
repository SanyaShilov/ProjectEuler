ANSWER =


def sum_d (n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
n = 1
lst = []
for i in range (2, 2000):
    for j in range(2, 100):
        num = i**j
        if sum_d(num) == i:
            lst.append(num)
            n += 1
lst.sort()
print(lst[30-1])


if __name__ == '__main__':
    print(main())
