ANSWER =


f = open('../txt/problem107.txt')
r = f.readlines()

ar = []
for i in range(len(r)):
    ar.append(r[i][:-1].split(','))
    for j in range(len(ar[-1])):
        if ar[-1][j] == '-':
            ar[-1][j] = 0
        else:
            ar[-1][j] = int(ar[-1][j])

leng = len(ar)

def minar (ar):
    m = 1000
    mi = 0
    mj = 0
    for i in range(leng):
        for j in range(leng):
            a = ar[i][j]
            if a:
                if a < m:
                    m = a
                    mi = i
                    mj = j
    return mi, mj

mn = minar(ar)
st = set(mn)
sm = ar[mn[0]][mn[1]]

def connect (ar, st):
    m = 1000
    mi = 0
    mj = 0
    for i in st:
        for j in range(leng):
            if j not in st:
                a = ar[i][j]
                if a:
                    if a < m:
                        m = a
                        mi = i
                        mj = j
    st.add(mj)
    return ar[mi][mj]

for i in range(leng-2):
    sm += connect(ar, st)

s = 0
for i in range(leng):
    for j in range(leng):
        s += ar[i][j]
s //= 2
print(s-sm)


if __name__ == '__main__':
    print(main())
