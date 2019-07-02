ANSWER =


nom = []
denom = []
for i in range(1, 10):
    for a in range(1, 10):
        for b in range(a+1, 10):
            if (10*i+a)/(10*b+i) == a/b:
                nom.append(10*i+a)
                denom.append(10*b+i)
            if (10*a+i)/(10*i+b) == a/b:
                nom.append(10*a+i)
                denom.append(10*i+b)
a = 1
for k in denom:
    a *= k
for k in nom:
    a //= k
print(a)
# 16 64 1/4
# 26 65 2/5
# 19 95 1/5
# 49 98 1/2


if __name__ == '__main__':
    print(main())
