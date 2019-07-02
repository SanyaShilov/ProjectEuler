import euler


ANSWER =


lst = euler.totientlist(10000000)

def is_permutation (a, b):
    s = []
    while a:
        s.append(a % 10)
        a //= 10
    try:
        while b:
            s.remove(b % 10)
            b //= 10
        if s:
            return False
        return True
    except:
        return False

def is_permutation (a, b):
    return sorted(str(a)) == sorted(str(b))
 
minimum = 10000
n = 0
sorted_strings = [sorted(str(i)) for i in range(10000000)]
for i in range(2, 10000000):
    fi = lst[i]
    if sorted_strings[i] == sorted_strings[fi]:
        m = i/fi
        if m < minimum:
            minimum = m
            n = i
print(n)


if __name__ == '__main__':
    print(main())
