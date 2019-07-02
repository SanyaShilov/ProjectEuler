ways = [0 for i in range(55)]
ways[0] = 1
for i in range(1, 51):
    ways[i] += ways[i-1] # black block
    if i >= 3:
        ways[i] += 1 # one red block
    for j in range(i-3):
        ways[i] += ways[i-j-4]
print(ways[50])
