leng = 8
height = 3

arwall = []
arind = [0]
arbuild = [[0 for i in range(leng+1)]]
while arind :
    
    ind = arind.pop()
    build = arbuild.pop()
    if ind == leng-3 :
        arwall.append(build)
        continue
    if ind == leng-2 :
        arwall.append(build)
        continue
    if ind == leng-1 :
        continue
    arind.append(ind+2)
    newbuild = build[:]
    newbuild[ind+2] = 1
    arbuild.append(newbuild)
    
    arind.append(ind+3)
    newbuild = build[:]
    newbuild[ind+3] = 1
    arbuild.append(newbuild)

l = len(arwall)
print(l)

can = [[1 for i in range(l)] for j in range(l)]
for i in range(l) :
    if not i % 100 :
        print(i)
    for j in range(i+1, l) :
        for k in range(leng) :
            if arwall[i][k] & arwall[j][k] :
                can[i][j] = 0
                break

            
for i in range(l) :
    can[i][i] = 0
    for j in range(i+1, l) :
        can[j][i] = can[i][j]
        
print('done')
arcount = [1 for i in range(l)]
for h in range(height-1) :
    print(h)
    newcount = [0 for i in range(l)]
    for i in range(l) :
        c = arcount[i]
        for j in range(l) :
            if can[i][j] :
                newcount[j] += c
    arcount = newcount
print(sum(arcount))
