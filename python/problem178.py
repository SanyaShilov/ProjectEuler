import itertools

digits = [i for i in range(10)]
allsets = []
for i in range(1, 11):
    for st in itertools.combinations(digits, i):
        allsets.append(set(st))

lensets = len(allsets)
arsets = []
arnums = []

for i in range(lensets):
    arsets.append([])
    for j in range(10):
        arsets[i].append(allsets.index(allsets[i].union({j})))
    arnums.append([0 for k in range(10)])

for i in range(1, 10):
    arnums[allsets.index({i})][i] = 1

res = 0
count = 40 - 1
ind = allsets.index({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
for _ in range(count):
    newar = [[0 for k in range(10)] for j in range(lensets)]
    for i in range(lensets):
        for j in range(9):
            newar[arsets[i][j]][j] += arnums[i][j+1]
            newar[arsets[i][j+1]][j+1] += arnums[i][j]
    arnums = newar
    s = sum(arnums[ind])
    print(s)
    res += s
print(res)


if __name__ == '__main__':
    print(main())
