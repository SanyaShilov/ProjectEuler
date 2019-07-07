ANSWER =


f = open('../txt/problem107.txt')
r = f.readlines()

lst = []
for i in range(len(r)):
    lst.append(r[i][:-1].split(','))
    for j in range(len(lst[-1])):
        if lst[-1][j] == '-':
            lst[-1][j] = 0
        else:
            lst[-1][j] = int(lst[-1][j])

leng = len(lst)

def minar (lst):
    m = 1000
    mi = 0
    mj = 0
    for i in range(leng):
        for j in range(leng):
            a = lst[i][j]
            if a:
                if a < m:
                    m = a
                    mi = i
                    mj = j
    return mi, mj

mn = minar(lst)
st = set(mn)
sm = lst[mn[0]][mn[1]]

def connect (lst, st):
    m = 1000
    mi = 0
    mj = 0
    for i in st:
        for j in range(leng):
            if j not in st:
                a = lst[i][j]
                if a:
                    if a < m:
                        m = a
                        mi = i
                        mj = j
    st.add(mj)
    return lst[mi][mj]

for i in range(leng-2):
    sm += connect(lst, st)

s = 0
for i in range(leng):
    for j in range(leng):
        s += lst[i][j]
s //= 2
print(s-sm)


if __name__ == '__main__':
    print(main())
