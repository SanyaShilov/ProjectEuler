ANSWER =


s = 0
for i in range (2, 300000):
    ar = [int(d) for d in str(i)]
    if i == sum(k**5 for k in ar):
        s += i
print(s)


if __name__ == '__main__':
    print(main())
