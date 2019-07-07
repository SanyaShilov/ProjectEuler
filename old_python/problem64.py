def calc (nn):
    sq = nn**0.5
    tr = int(sq)
    start = add = -tr
    d = 1
    l = 0
    while True:
        l += 1
        wtf = nn-add*add
        d = wtf//d
        tr = int((sq-add)/d)
        add = -add - tr*d
        if d == 1 and add == start:
            break
    return l 
        
squares = [i*i for i in range(1000)]
notsquares = [i for i in range(1, 10001) if i not in squares]

result = 0
for num in notsquares:
    c = calc(num)
    if c % 2:
        result += 1
print(result)
