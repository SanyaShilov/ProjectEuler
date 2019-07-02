ANSWER =


def is_square (n):
    nn = n**0.5
    return nn.is_integer()


'''
s = 0
sq = [i for i in range(1, 10001)]
for i in sq:
    if is_square(i):
        print(i)
        s += 1
print(s)
'''

def calc (nn):
    sq = nn**0.5
    tr = int(sq)
    start = add = -tr
    d = 1
    l = 0
    lst = [tr]
    while True:
        l += 1
        wtf = nn-add*add
        d = wtf//d
        tr = int((sq-add)/d)
        lst.append(tr)
        add = -add - tr*d
        if d == 1 and add == start:
            break
    return lst

lst = calc(5)

n = 0
s = 0
i = 0
isq1 = 3
sq5 = 45 # bigger


N = 2
while n < 5:
    N += 6
    num = N*N + 1
    while num > sq5:
        isq1 += 1
        sq5 = 5*isq1*isq1
    if num == sq5:
        n += 1
        #print(N, isq1)
        isq1 += 1
        sq5 = 5*isq1*isq1
        s += isq1
    
    N += 14
    num = N*N + 1
    while num > sq5:
        isq1 += 1
        sq5 = 5*isq1*isq1
    if num == sq5:
        n += 1
        #print(N,  isq1)
        isq1 += 1
        sq5 = 5*isq1*isq1
        s += isq1

    N += 6
    num = N*N + 1
    while num > sq5:
        isq1 += 1
        sq5 = 5*isq1*isq1
    if num == sq5:
        n += 1
        #print(N, isq1)
        isq1 += 1
        sq5 = 5*isq1*isq1
        s += isq1

    N += 4
    num = N*N + 1
    while num > sq5:
        isq1 += 1
        sq5 = 5*isq1*isq1
    if num == sq5:
        n += 1
        #print(N, isq1)
        isq1 += 1
        sq5 = 5*isq1*isq1
        s += isq1

lst = [17, 305]
for i in range(10):
    lst.append(18*lst[-1]-lst[-2])
print(sum(lst))


if __name__ == '__main__':
    print(main())
