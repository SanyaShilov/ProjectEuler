import itertools

for i, permutation in enumerate(itertools.permutations(tuple(i for i in range(10)))):
    if i == 999999:
        s = 0
        for n in permutation:
            s = s * 10 + n
        print(s)
        break
