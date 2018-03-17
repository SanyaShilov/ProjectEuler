s = 0
d = [str(k) for k in range(10)]
dd4 = [str(k) for k in range(0, 10, 2)]
for a6 in ['5', '0'] :
    for a4 in dd4 :
        d46 = [k for k in d if k != a4 and k != a6]
        for a7 in d46 :
            d467 = [k for k in d46 if k != a7]
            for a8 in d467 :
                if (int(a6)-int(a7)+int(a8)) % 11 == 0 :
                    d4678 = [k for k in d467 if k != a8]
                    aa78 = 100*int(a7)+10*int(a8)
                    for a9 in d4678 :
                        if (aa78+int(a9)) % 13 == 0 :
                            d46789 = [k for k in d4678 if k != a9]
                            aa89 = 100*int(a8)+10*int(a9)
                            for a10 in d46789 :
                                if (aa89+int(a10)) % 17 == 0 :
                                    d4678910 = [k for k in d46789 if k != a10]
                                    for a3 in d4678910 :
                                        d34678910 = [k for k in d4678910 if k != a3]
                                        for a5 in d34678910 :
                                            if (int(a3)+int(a4)+int(a5)) % 3 == 0 :
                                                if int(a5+a6+a7) % 7 == 0 :
                                                    d345678910 = [k for k in d34678910 if k != a5]
                                                    for a2 in d345678910 :
                                                        d2345678910 = [k for k in d345678910 if k != a2]
                                                        for a1 in d2345678910 :
                                                            n = int(a1+a2+a3+a4+a5+a6+a7+a8+a9+a10)
                                                            print(n)
                                                            s += n
print(s)            
