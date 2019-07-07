import itertools

def check (lst):
    prev_max = lst[0]
    for i in range(2, len(lst)):
        s = set()
        for comb in itertools.combinations(lst, i):
            sm = sum(comb)
            if sm <= prev_max:
                return False
            if sm in s:
                return False
            s.add(sm)
        prev_max = max(s)
    return True

lst = [sorted([int(k) for k in l.split(',')], reverse = True)
      for l in open('../txt/problem105.txt').readlines()]
print(lst)
s = 0
for a in lst:
    if check(a):
        print(a)
        s += sum(a)


if __name__ == '__main__':
    print(main())
