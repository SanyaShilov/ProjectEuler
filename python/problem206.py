ANSWER =


print(len(str((10**9)**2)))
i = 10**9+10**7+10**5+10**3+10
print(i**2)
print((10**9+int(10**9/2000))**2)
print((10**9+5*10**1)**2)

while True:
    i += 10
    s = str(i**2)
    print(s)
    
    if s[0] == '1':
        if s[2] == '2':
            if s[4] == '3':
                if s[6] == '4':
                    if s[8] == '5':
                        if s[10] == '6':
                            if s[12] == '7':
                                if s[14] == '8':
                                    if s[16] == '9':
                                        if s[18] == '0':
                                            print(i)
                                            break
    
    if s[2] > '2':
        i += 400000
    elif s[2] < '1':
        i += 400000
    elif s[4] > '3':
        i += 4000
    elif s[4] < '2':
        i += 4000
    elif s[6] > '4':
        i += 40
    elif s[6] < '3':
        i += 40
#1389019170


if __name__ == '__main__':
    print(main())
