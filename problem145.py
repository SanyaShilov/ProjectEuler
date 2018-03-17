s = 0
for a in range(1, 10) :
    for b in range(1, 10) :
        if a+b > 9 :
            break
        if (a+b) % 2 :
            #print(10*a+b, 10*b+a, 11*(a+b))
            s += 1
            
for a in range(1, 10) :
    for b in range(5) :
        for c in range(10) :
            if a+c < 10 :
                continue
            if (a+c) % 2 :
                #print(100*a+10*b+c, 100*c+10*b+a, 101*a+11*b+101*c)
                s += 1

for a in range(1, 10) :
    for b in range(10) :
        for c in range(10) :
            if c + b > 9 :
                break
            if (c+b) % 2 :
                for d in range(1, 10) :
                    if a+d > 9 :
                        break
                    if (a+d) % 2 :
                        s += 1

for a in range(1, 10) :
    for b in range(10) :
        for c in range(10) :
            for d in range(10) :
                if c + d > 9 :
                    break
                if (c + d) % 2 :
                    for e in range(10) :
                        if b + e > 9 :
                            break
                        if (b+e) % 2 :
                            for f in range(1, 10) :
                                if a + f > 9 :
                                    break
                                if (a+f) % 2 :
                                    s += 1

for a in range(1, 10) :
    for b in range(10) :
        for c in range(10) :
            for d in range(5) :
                for e in range(10) :
                    if c + e < 10 :
                        continue
                    if (c+e) % 2 :
                        for f in range(10) :
                            if b + f > 9 :
                                break
                            if (b+f) % 2 == 0 :
                                for g in range(1, 10) :
                                    if a + g < 10 :
                                        continue
                                    if (a+g) % 2 :
                                        s += 1

for a in range(1, 10) :
    for b in range(10) :
        for c in range(10) :
            for d in range(10) :
                for e in range(10) :
                    if d + e > 9 :
                        break
                    if (d+e) % 2 :
                        for f in range(10) :
                            if f + c > 9 :
                                break
                            if (f+c) % 2 :
                                for g in range(10) :
                                    if g + b > 9 :
                                        break
                                    if (g+b)% 2 :
                                        for h in range(1, 10) :
                                            if a + h > 9 :
                                                break
                                            if (a+h) % 2 :
                                                s += 1




print(s)
