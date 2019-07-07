lst = open('../txt/problem022.txt').readlines()
lst = lst[0][1:-1].split('\",\"')
lst.sort()
def s (w):
    r = 0
    l = len(w)
    for i in range(l):
        r += ord(w[i])
    return r - l*64
total = 0
for i in range(len(lst)):
    total += (i+1)*s(lst[i])
print(total)
