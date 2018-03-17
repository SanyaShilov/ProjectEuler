b = bin(10**25)[2:]

def calc (b, start = 0) :
    print(b)
    res = 1
    for i in range(start, lll) :
        if b[i] != '0' :
            if b[i+1] == '0' :
                if i > 0 :
                    if b[i-1] == '0' :
                        start = i + 1
                    else :
                        start = 0
                wtf = b[:i]+chr(ord(b[i])-1)+'2'+b[i+2:]
                res += calc(wtf, start)
    return res



def calc (b) :
    l = len(b)
    rf = b.rfind('1')
    if b.count('1') == 1 :
        return l-rf
    return calc(b[:rf])+(l-rf-1)*calc(b[:rf]+'0')

print(calc(b))
