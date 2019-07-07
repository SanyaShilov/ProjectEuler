import array


ANSWER =


def sumdivisors (n):
    i = (1 for i in range(n+1))
    result = array.array('L', i)
    for i in range(2, n//2):
        for j in range(2, n//i+1):
            result[i*j] += i
    return result

lst = sumdivisors(1000000)
mxl = 0
value = 0

def length (start):
    global mxl
    global value
    l = 1
    ind = lst[start]
    while ind > start:
        if l > 100:
            return
        if ind >= 1000000:
            return
        ind = lst[ind]
        l += 1
    if ind == start:
        if l > mxl:
            mxl = l
            value = start

for i in range(1, 1000000):
    length(i)

print(value)


if __name__ == '__main__':
    print(main())
