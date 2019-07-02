ANSWER =


la = [2, 3, 4]
m = 12
nex = 5
newtwo = 8
twoes = 2
l = 3
p = twoes / l
stop = 1 / 12345
while p >= stop:
    if nex == newtwo:
        twoes += 1
        newtwo *= 2
    l += 1
    p = twoes / l
    nex += 1
print((nex-1)*(nex-1)-nex+1)


if __name__ == '__main__':
    print(main())
