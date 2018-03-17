# 12952 <= 1000000

def is_inc (n) :
    s = str(n)
    for i in range(len(s)-1) :
        if s[i] > s[i+1] :
            return False
    return True

def is_dec (n) :
    s = str(n)
    for i in range(len(s)-1) :
        if s[i] < s[i+1] :
            return False
    return True

def is_bounc (n) :
    if is_inc(n) :
        return False
    if is_dec(n) :
        return False
    return True


i = 21780
s = i - 2178
while s/i < 0.99 :
    i += 1
    s += is_bounc(i)
print(i)
