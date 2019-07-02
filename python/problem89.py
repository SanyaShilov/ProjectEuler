ANSWER =


f = open('../txt/problem089.txt')
r = f.readlines()

def clean (s):
    if s[-1] == '\n':
        return s[:-1]
    return s

def number (s):
    if s == 'M':
        return 1000
    if s == 'D':
        return 500
    if s == 'C':
        return 100
    if s == 'L':
        return 50
    if s == 'X':
        return 10
    if s == 'V':
        return 5
    if s == 'I':
        return 1

def RomanToTen (s):
    res = 0
    last = number(s[0])
    for i in range(1, len(s)):
        temp = number(s[i])
        if temp <= last:
            res += last
        else:
            res -= last
        last = temp
    res += last
    return res

def TenToRoman (n):
    res = ''
    res += 'M'*(n//1000)
    n %= 1000
    r = n//100
    if r == 9:
        res += 'CM'
    elif r == 4:
        res += 'CD'
    else:
        if r >= 5:
            res += 'D'
        res += (r%5)*'C'
    n %= 100
    r = n//10
    if r == 9:
        res += 'XC'
    elif r == 4:
        res += 'XL'
    else:
        if r >= 5:
            res += 'L'
        res += (r%5)*'X'
    r = n%10
    if r == 9:
        res += 'IX'
    elif r == 4:
        res += 'IV'
    else:
        if r >= 5:
            res += 'V'
        res += (r%5)*'I'
    return res


res = 0   
for i in range(len(r)):
    s = clean(r[i])
    n = RomanToTen(s)
    s2 = TenToRoman(n)
    res = res + len(s) - len(s2)
print(res)


if __name__ == '__main__':
    print(main())
