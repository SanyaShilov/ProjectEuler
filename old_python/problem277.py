def backward (st):
    res = 1
    for k in st[::-1]:
        if k == 'D':
            res *= 3
        if k == 'd':
            res = (res*3+1)//2
        if k == 'U':
            res = (res*3-2)//4
    return res

def forward (n):
    res = ''
    while n > 1:
        if n % 3 == 0:
            res += 'D'
            n //= 3
            continue
        if n % 3 == 1:
            res += 'U'
            n = (4*n+2)//3
            continue
        if n % 3 == 2:
            res += 'd'
            n = (2*n-1)//3
    return res

def forward_eq (n, st):
    res = ''
    for i in range(len(st)):
        if not n % 3:
            if st[i] != 'D':
                return False
            n //= 3
        elif n % 3 == 1:
            if st[i] != 'U':
                return False
            n = (4*n+2)//3
        else:
            if st[i] != 'd':
                return False
            n = (2*n-1)//3
    return True
    
st = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'



n = 0
for k in range(1, len(st)+1):
    for i in range(n, 3**(k+1), 3**(k-1)):
        if forward(i)[:k] == st[:k]:
            n = i
            break
        
while n < 10**15:
    n += 3**30
    
print(n)


