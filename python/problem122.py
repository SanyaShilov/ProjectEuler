ANSWER =


lst = [[], [{1}]]
LIMIT = 200
for i in range(2, LIMIT+1):
    lst.append([])
    for j in range(i//2, i):
        d = i - j
        for st in lst[j]:
            if d in st:
                lst[-1].append(st.union({i}))
    m = 10**10
    for st in lst[-1]:
        if len(st) < m:
            m = len(st)
    for st in lst[-1][:]:
        if len(st) > m:
            lst[-1].remove(st)

s = 0
for i in range(1, LIMIT+1):
    s += len(lst[i][0])-1 # -1 because we don't compute the n**1
print(s)


if __name__ == '__main__':
    print(main())
