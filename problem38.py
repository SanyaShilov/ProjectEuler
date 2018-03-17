s = set('123456789')
m = 0
for i in range(9001, 10000) :
    if set(str(i)+str(i*2)) == s :
        if i > m :
            m = i
print(int(str(m)+str(m*2)))
        
