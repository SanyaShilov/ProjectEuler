lst = [l.split()[0] for l in open('../txt/problem079.txt').readlines()]

s = set()
for n in lst:
    for l in n:
        s.add(l)
        
before = {}
for l in s:
    before[l] = set()
    for n in lst:
        i = n.find(l)
        if i != -1:
            for j in range(i):
                before[l].add(n[j])

password = ''
for _ in range(len(before)):
    for l in before.copy():
        if before[l] == set():
            password += l
            for ll in before:
                before[ll].discard(l)
            before.pop(l)
print(password)
        
