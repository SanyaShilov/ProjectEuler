ANSWER =


ar = open('../txt/problem022.txt').readlines()
ar = ar[0][1:-1].split('\",\"')
ar.sort()
def s (w):
    r = 0
    l = len(w)
    for i in range(l):
        r += ord(w[i])
    return r - l*64
total = 0
for i in range(len(ar)):
    total += (i+1)*s(ar[i])
print(total)


if __name__ == '__main__':
    print(main())
