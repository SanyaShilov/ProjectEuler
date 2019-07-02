import itertools


ANSWER =


dig = [i for i in range(10)]

have = []
for ind in itertools.combinations(dig, 6):
    have.append([i in ind for i in range(10)])

s = 0
l = len(have)
for i in range(l):
    need = set()
    needone = set()
    need69 = False
    
    if not have[i][0]:
        if not have[i][1]:
            continue
        if not have[i][4]:
            continue
        if not have[i][6] and not have[i][9]:
            continue
        need.add(0)
    else:
        if not have[i][1]:
            need.add(1)
        else:
            needone.add((0, 1))
        if not have[i][4]:
            need.add(4)
        else:
            needone.add((0, 4))
        if not have[i][6] and not have[i][9]:
            need69 = True
        else:
            needone.add((0, 6, 9))

    if not have[i][1]:
        if not have[i][8]:
            continue
        if not have[i][6] and not have[i][9]:
            continue
        need.add(1)
    else:
        if not have[i][8]:
            need.add(8)
        else:
            needone.add((1, 8))
        if not have[i][6] and not have[i][9]:
            need69 = True
        else:
            needone.add((1, 6, 9))

    if not have[i][2]:
        if not have[i][5]:
            continue
        need.add(2)
    else:
        if not have[i][5]:
            need.add(5)
        else:
            needone.add((2, 5))

    if not have[i][3]:
        if not have[i][6] and not have[i][9]:
            continue
        need.add(3)
    else:
        if not have[i][6] and not have[i][9]:
            need69 = True
        else:
            needone.add((3, 6, 9))

    if not have[i][4]:
        if not have[i][6] and not have[i][9]:
            continue
        need.add(4)
    else:
        if not have[i][6] and not have[i][9]:
            need69 = True
        else:
            needone.add((4, 6, 9))

    for j in range(i, l):
        passedneed = True
        for k in need:
            if not have[j][k]:
                passedneed = False
                break
        if not passedneed:
            continue
        if need69:
            if not have[j][6] and not have[j][9]:
                continue
        for nn in needone:
            passed = False
            for n in nn:
                if have[j][n]:
                    passed = True
                    break
            if not passed:
                break
        if not passed:
            continue
        s += 1
print(s)


if __name__ == '__main__':
    print(main())
