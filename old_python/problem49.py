ar = [i for i in range(10000)]
for i in range(2, 100):
    for j in range(2, 10000//i+100):
        try:
            ar[i*j] = 0
        except:
            pass

for d in range(500, 4500):
    for i in range(1000, 10000-2*d):
        if ar[i] != 0:
            if ar[i] != 1487:
                if ar[i+d] != 0:
                    if ar[i+2*d] != 0:
                        s1 = set(str(ar[i]))
                        s2 = set(str(ar[i+d]))
                        s3 = set(str(ar[i+2*d]))
                        if s1 == s2:
                            if s1 == s3:
                                print(str(ar[i])+str(ar[i+d])+str(ar[i+2*d]))
                                break
