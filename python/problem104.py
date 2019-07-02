ANSWER =


a, b = 1, 1
i = 2
s = set('123456789')
a5 = (1 + 5**0.5)/2
b5 = (1 - 5**0.5)/2
q5 = 5**0.5
tens = 10**14
tab = [0, 1, 1]

def fib (n): # первые 15 цифр
    a = tab[1]
    b = tab[2]
    for i in range(n-tab[0]):
        a *= a5
        b *= b5
        if a > tens:
            a /= 10
        if b > tens:
            b /= 10
    tab[:] = [n, a, b]
    return round((a-b)/q5)

while 1:
    a, b = b, a+b
    i += 1
    st = str(b)[-9:]
    end = set(st)
    if end == s:
        st2 = str(fib(i))[:9]
        begin = set(st2)
        if begin == s:
            print(i)
            break
    b = int(st)


if __name__ == '__main__':
    print(main())
