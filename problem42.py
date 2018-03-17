ar = open('p042.txt').readlines()
ar = ar[0][1:-1].split('\",\"')
tr = [k*(k+1)//2 for k in range(1, 50)]
def value (w) :
    s = 0
    for i in range(len(w)) :
        s += ord(w[i])
        s -= 64
    return s
num = 0
for k in ar :
    if value(k) in tr :
        num += 1
print(num)
