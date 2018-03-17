# dynamic programming

ways = [0 for i in range(55)]
ways[0] = 1
for i in range(1, 51) :
    for j in range(1, 5) :
        if i >= j :
            ways[i] += ways[i-j]
print(ways[50])
