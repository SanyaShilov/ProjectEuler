ANSWER =


def square (n):
    return sum(int(k)**2 for k in str(n))
tab_1 = [0 for k in range(10000)]
tab_89 = [0 for k in range(10000)]
for k in [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97]:
    tab_1[k] = k
for k in [2, 3, 4, 5, 6, 8, 9, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 29, 30, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81, 83, 84, 85, 87, 88, 89, 90, 92, 93, 95, 96, 98, 99]:
    tab_89[k] = k
s = 0
for i in range(1, 10000000):
    temp = square(i)
    while 1:
        if tab_1[temp] != 0:
            break
        if tab_89[temp] != 0:
            s += 1
            break
        temp = square(temp)
print(s)


if __name__ == '__main__':
    print(main())
