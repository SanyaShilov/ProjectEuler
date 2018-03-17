# LESS THAN 62771113
# 6277***3 is 8-length
# now check ...*n**n
# LESS THAN 31204009
# now check ...**n*n
# nothing new
# now check ...***nn
# nothing new
# now check ...***nnn
# fuck!
# now check ...*n**nn
# мы поймали их за яйца
# LESS THAN 2090021
# now check ...**n*nn
# nothing
# now check ...**nn*n
# now check ...*nn**n
# now check ...*n*n*n

import euler
import array
length = 10000000
mas = array.array('L', (0 for i in range(length)))
primelist = euler.primelist(length)
print('created')

def faster (n) :
    rest = n % 10

    

    
    
    n //= 10
    dig1 = n % 10

    n //= 10
    rest *= 10
    rest += n % 10

    n //= 10
    if dig1 != n % 10 :
        return False, None

    
    
    n //= 10
    rest *= 10
    rest += n % 10
    
    

    
    
    n //= 10
    if dig1 != n % 10 :
        return False, None
    
    n //= 10
    while n :
        rest *= 10
        rest += n % 10
        n //= 10
        
    return True, rest




for pr in primelist :
    res = faster(pr)
    if res[0] :
        mas[res[1]] += 1
print(max(mas))
