# dynamic programming

ar = [[int(i) for i in l.split()] for l in open('p067.txt').readlines()]
mx = ar[0]
for i in range(1, len(ar)) :
    mx = [ar[i][0]+mx[0]]+[ar[i][j]+max(mx[j-1], mx[j]) for j in range(1, i)]+[ar[i][-1]+mx[-1]]
print(max(mx))    
