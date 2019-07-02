def div (n):
    d = 0
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                d = i
                if d > 47:
                    return False
                n = n // i
                break
    return True

ar4 = [i for i in range(4000)]

for i in range(2, 70):
    for j in range(2, 4000//i+70):
        try:
            ar4[i*j] = 0
        except:
            pass
ar4[1] = 0
s4 = [i for i in ar4 if i != 0]
l4 = len(s4)
print('1')
print(s4.index(47))
ar16 = [i for i in range(16000)]
for i in range(s4.index(31)+1, l4):
    
    t = s4[i]
    print(t)
    for j in range(1, 16000//t+t):
        try:
            ar16[t*j] = 0
        except:
            pass
ar16[1] = 0
print(ar16)


if __name__ == '__main__':
    print(main())
