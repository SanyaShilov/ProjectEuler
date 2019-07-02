r = 0.00000000137
print(1/r)
m = 729927001
print(r*m)
l = 56789
print(l*m)
while True:
    a = l*m
    if a % 100000 == 99999:
        break
    m -= 10
print(m)
print(l*m, r*m)

# 729909891


if __name__ == '__main__':
    print(main())
