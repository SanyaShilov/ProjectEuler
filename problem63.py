s = 0
for i in range(1, 100) :
    for j in range(1, 200) :
        if len(str(i**j)) == j :
            s += 1
print(s)
