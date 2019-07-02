import euler


ANSWER =


ar = euler.prime_list(1000000)

def fill (n): #  нечетное
    tab = [[0 for i in range(n)] for j in range(n)]
    c = n // 2
    tab[c][c] = 1
    num = 2
    for i in range (2, n, 2):
        for j in range(i):
            tab[c+1-i//2+j][c+i//2] = num
            num += 1
        for j in range(i):
            tab[c+i//2][c+i//2-1-j] = num
            num += 1
        for j in range(i):
            tab[c-j+i//2-1][c-i//2] = num
            num += 1
        for j in range(i):
            tab[c-i//2][c+j-i//2+1] = num
            num += 1
    return tab

d = 2
pr = 3
al = 5
c = pr/al
temp = 9
while c >= 0.1:
    d += 2
    temp += d
    if euler.isprime(temp, ar):
        pr += 1
    temp += d
    if euler.isprime(temp, ar):
        pr += 1
    temp += d
    if euler.isprime(temp, ar):
        pr += 1
    temp += d
    al += 4
    c = pr/al
print(d+1)


if __name__ == '__main__':
    print(main())
