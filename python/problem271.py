s = 0
for i in range(153416670, 13082761331670030, 153416670):
    j = i+1
    if j*j*j % 13082761331670030 == 1:
        s += j
print(s)


if __name__ == '__main__':
    print(main())
