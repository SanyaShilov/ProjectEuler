ANSWER =


def d_sum (n):
    s = str(n)
    l = len(s)
    ds = 0
    for i in range(l):
        ds += ord(s[i])
    return ds-l*ord('0')

def result (n):
    m = n * 100
    sq = int(n**0.5)
    while len(str(sq)) < 100:
        m *= 100
        sq *= 10
        while sq**2 < m:
            sq += 1
        sq -= 1
    return d_sum(sq)

squares = [i**2 for i in range(1, 11)]
s = 0
for i in range(1, 101):
    if i not in squares:
        r = result(i)
        s += r
print(s)


if __name__ == '__main__':
    print(main())
