a, b = 1, 1
s = 0
while b < 4*10**6 :
    if not b % 2 :
        s += b
    a, b = b, a + b
print(s)    
