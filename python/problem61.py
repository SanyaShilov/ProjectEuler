ANSWER =


def condition (n):
    return len(str(n)) == 4 and str(n)[2] != '0'

d = [[k for k in (i*(3*i-2) for i in range(200)) if condition(k)],
     [k for k in (i*(5*i-3)//2 for i in range(200)) if condition(k)],
     [k for k in (i*(2*i-1) for i in range(200)) if condition(k)],
     [k for k in (i*(3*i-1)//2 for i in range(200)) if condition(k)],
     [k for k in (i*i for i in range(200)) if condition(k)],
     [k for k in (i*(i+1)//2 for i in range(200)) if condition(k)]]

starts = [[str(n)[:2] for n in lst] for lst in d]
ends = [[str(n)[2:] for n in lst] for lst in d]

nums = [[i] for i in range(len(d[0]))]
used = [[0] for n in d[0]]

while nums:
    num = nums.pop()
    use = used.pop()
    if len(use) == 6:
        if ends[use[-1]][num[-1]] == starts[use[0]][num[0]]:
            print(sum(d[use[i]][num[i]] for i in range(len(use))))
    else:
        for i in range(1, 6):
            if i not in use:
                for j in range(len(starts[i])):
                    if ends[use[-1]][num[-1]] == starts[i][j]:
                        newuse = use+[i]
                        newnum = num+[j]
                        used.append(newuse)
                        nums.append(newnum)


if __name__ == '__main__':
    print(main())
