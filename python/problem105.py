import itertools


def check(st):
    prev_max = st[0]
    for i in range(2, len(st)):
        combination_sums = set()
        for comb in itertools.combinations(st, i):
            combination_sum = sum(comb)
            if combination_sum <= prev_max:
                return False
            if combination_sum in combination_sums:
                return False
            combination_sums.add(combination_sum)
        prev_max = max(combination_sums)
    return True


def main():
    lst = [
        sorted([int(n) for n in line.split(',')], reverse=True)
        for line in open('../txt/problem105.txt')
    ]
    total = 0
    for st in lst:
        if check(st):
            total += sum(st)
    return total


if __name__ == '__main__':
    print(main())
