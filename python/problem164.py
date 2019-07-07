ANSWER =


lst = [0 for i in range(1000)]
for i in range(1, 10):
    lst[i] = 1

sums = [a//100 + (a//10)%10 + a%10 for a in range(1000)]

for _ in range(19):
    newar = [0 for i in range(1000)]
    for i in range(1000):
        s = sums[i]
        n = (i%100)*10
        for j in range(10-s+i//100):
            newar[n+j] += lst[i]
    lst = newar
print(sum(lst))


if __name__ == '__main__':
    print(main())
