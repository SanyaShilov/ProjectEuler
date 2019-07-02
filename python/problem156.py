ANSWER =


count = 0
ten = 10
for i in range(100000001):
    count += str(i).count('2')
    if i == ten:
        print(i, count)
        ten *= 10
    if i == count:
        print(i, count)


if __name__ == '__main__':
    print(main())
