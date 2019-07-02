ar = [0 for i in range(1000)]
for i in range(1, 10):
    ar[i] = 1

sums = [a//100 + (a//10)%10 + a%10 for a in range(1000)]

for _ in range(19):
    newar = [0 for i in range(1000)]
    for i in range(1000):
        s = sums[i]
        n = (i%100)*10
        for j in range(10-s+i//100):
            newar[n+j] += ar[i]
    ar = newar
print(sum(ar))
