lst = [[int(i) for i in l.split()] for l in open('../txt/problem018.txt').readlines()]
mx = lst[0]
for i in range(1, len(lst)):
    mx = [lst[i][0]+mx[0]]+[lst[i][j]+max(mx[j-1], mx[j]) for j in range(1, i)]+[lst[i][-1]+mx[-1]]
print(max(mx))    
