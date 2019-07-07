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
    result = 0
    last = number(s[0])
    for i in range(1, len(s)):
        temp = number(s[i])
        if temp <= last:
            result += last
        else:
            result -= last
        last = temp
    result += last
    return result

def TenToRoman (n):
    result = ''
    result += 'M'*(n//1000)
    n %= 1000
    r = n//100
    if r == 9:
        result += 'CM'
    elif r == 4:
        result += 'CD'
    else:
        if r >= 5:
            result += 'D'
        result += (r%5)*'C'
    n %= 100
    r = n//10
    if r == 9:
        result += 'XC'
    elif r == 4:
        result += 'XL'
    else:
        if r >= 5:
            result += 'L'
        result += (r%5)*'X'
    r = n%10
    if r == 9:
        result += 'IX'
    elif r == 4:
        result += 'IV'
    else:
        if r >= 5:
            result += 'V'
        result += (r%5)*'I'
    return result


result = 0
for i in range(len(r)):
    s = clean(r[i])
    n = RomanToTen(s)
    s2 = TenToRoman(n)
    result = result + len(s) - len(s2)
print(result)


if __name__ == '__main__':
    print(main())
