# dynamic programming

m = 50

ways = [1]
while ways[-1] < 1000000 :
    ways.append(0)
    i = len(ways)-1
    ways[i] += ways[i-1]
    if i >= m :
        ways[i] += 1
    for j in range(i-m) :
        ways[i] += ways[i-j-m-1]

print(len(ways)-1)
