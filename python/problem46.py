ANSWER =


ar = [i for i in range(100000)]
for i in range(2, 320):
    for j in range(2, 100000//i+320):
        try:
            ar[i*j] = 0
        except:
            pass
ar[1] = 0
sq = [2*i**2 for i in range(1, 101)]
big = []
a = 33
while True:
    a += 2
    if ar[a] != 0:
        pass
    else:
        maybe = 1
        for i in range(100):
            q = a - sq[i]
            if q > 0:
                if ar[a - sq[i]] != 0:
                    maybe = 0
                    break
            else:
                break
        if maybe == 1:
            print(a)
            break


if __name__ == '__main__':
    print(main())
