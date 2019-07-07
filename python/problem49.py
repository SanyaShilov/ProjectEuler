ANSWER =


lst = [i for i in range(10000)]
for i in range(2, 100):
    for j in range(2, 10000//i+100):
        try:
            lst[i*j] = 0
        except:
            pass

for d in range(500, 4500):
    for i in range(1000, 10000-2*d):
        if lst[i] != 0:
            if lst[i] != 1487:
                if lst[i+d] != 0:
                    if lst[i+2*d] != 0:
                        s1 = set(str(lst[i]))
                        s2 = set(str(lst[i+d]))
                        s3 = set(str(lst[i+2*d]))
                        if s1 == s2:
                            if s1 == s3:
                                print(str(lst[i])+str(lst[i+d])+str(lst[i+2*d]))
                                break


if __name__ == '__main__':
    print(main())
