ANSWER =


once = set()
more = set()
LIMIT = 50*10**6
for d in range(1, LIMIT//4+1):
    const = 3*d*d
    mn = 2*d
    for z in range(1, d+1):
        n = const + z*mn - z*z
        if n >= LIMIT:
            break
        if n in once:
            more.add(n)
        else:
            once.add(n)
    for z in range(3*d-1, d, -1):
        n = const + z*mn - z*z
        if n >= LIMIT:
            break
        if n in once:
            more.add(n)
        else:
            once.add(n)
for k in more:
    if k in once:
        once.discard(k)
print(len(once))

# about 10 minutes


if __name__ == '__main__':
    print(main())
