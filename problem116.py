# dynamic programming

redways = [0 for i in range(55)]
redways[0] = 1
for i in range(1, 51) :
    for j in (1, 2) :
        if i >= j :
            redways[i] += redways[i-j]

greenways = [0 for i in range(55)]
greenways[0] = 1
for i in range(1, 51) :
    for j in (1, 3) :
        if i >= j :
            greenways[i] += greenways[i-j]

blueways = [0 for i in range(55)]
blueways[0] = 1
for i in range(1, 51) :
    for j in (1, 4) :
        if i >= j :
            blueways[i] += blueways[i-j]

print(redways[50]+greenways[50]+blueways[50]-3)
