ANSWER =


ar = [i for i in range(1000000)]
for i in range(2, 1000):
    for j in range(2, 1000000//i+1000):
        try:
            ar[i*j] = 0
        except:
            pass
ar[1] = 0
prime = []
for i in range(1000000):
    if ar[i] != 0:
        prime.append(i)
l = len(prime)
m = 0

for i in range(3, l, 2):
    s = sum(prime[3:i+3])
    if s > 1000000:
        break
    if ar[s] != 0:
        if s > m:
            m = s          
print(m)


if __name__ == '__main__':
    print(main())
