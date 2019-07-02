ANSWER =


def f (x, y):
    s = 0
    for i in range(0, x):
        for j in range(0, y):
            s += (x-i)*(y-j)
    return s

neari, nearj = 0, 0
nearm = 10**10
for i in range(100):
    for j in range(100):
        near = abs(2000000-f(i, j))
        if near < nearm:
            nearm = near
            neari, nearj = i, j
print(neari*nearj)


if __name__ == '__main__':
    print(main())
