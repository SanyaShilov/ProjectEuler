import itertools

def check (ar):
    prev_max = ar[0]
    for i in range(2, len(ar)):
        s = set()
        for comb in itertools.combinations(ar, i):
            sm = sum(comb)
            if sm <= prev_max:
                return False
            if sm in s:
                return False
            s.add(sm)
        prev_max = max(s)
    return True

ar = [sorted([int(k) for k in l.split(',')], reverse = True)
      for l in open('../txt/problem105.txt').readlines()]
print(ar)
s = 0
for a in ar:
    if check(a):
        print(a)
        s += sum(a)


if __name__ == '__main__':
    print(main())
