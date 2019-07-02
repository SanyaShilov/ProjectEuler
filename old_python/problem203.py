ar = [i for i in range(11243250)]
for i in range(2, 3360):
    for j in range(2, 11243250//i+3360):
        try:
            ar[i*j] = 0
        except:
            pass
ar[1] = 0
print('ar')
sq = [i**2 for i in ar if i != 0]
print(sq[:10])
        
pascal = [[0 for i in range(51)] for j in range(51)]
for i in range(51):
    pascal[i][0] = 1
m = 0
for i in range(1, 51):
    for j in range(i+1):
        pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]
        if pascal[i][j] > m:
            m = pascal[i][j]
print(m)
s = set()
for i in range(51):
    for j in range(51):
        s = s.union({pascal[i][j]})
print(len(s))
n = set(s)
for q in sq:
    for k in s:
        if k % q == 0:
            n.discard(k)
print(sum(n))
