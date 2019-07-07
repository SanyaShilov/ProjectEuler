ANSWER =


def is_palindrom (n):
    lst = []
    while n:
        lst.append(n%10)
        n //= 10
    l = len(lst)
    while l > 1:
        if lst[0] != lst[-1]:
            return False
        lst.pop()
        lst.pop(0)
        l -= 2
    return True

pal = set()

LIMIT = 10**8

def gpal (b):
    bb = b*(b+1)*(2*b+1)
    for a in range(b-2, -1, -1):
        result = (bb-a*(a+1)*(2*a+1))//6
        if result > LIMIT:
            break
        if is_palindrom(result):
            pal.add(result)

for i in range(1, 10000):
    gpal(i)

r = 0
for p in pal:
    r += p
print(r)


if __name__ == '__main__':
    print(main())
