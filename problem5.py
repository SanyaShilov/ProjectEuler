import euler

limit = 20
primelist = euler.primelist(limit+1)
result = 1
for i in range(len(primelist)) :
    pr = primelist[i]
    while pr < limit :
        pr *= primelist[i]
    pr //= primelist[i]
    result *= pr
print(result)
    
