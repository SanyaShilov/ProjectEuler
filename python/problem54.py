ANSWER =


f = open('../txt/problem054.txt')
r = f.readlines()
ar = [k for k in r]

def checkFlush (strhand):
    m = strhand[0][1]
    for k in strhand:
        if k[1] != m:
            return False
    return True

def checkStraight (sorthand):
    a = sorthand[0]
    for i in range(1, 5):
        if sorthand[i]-a != i:
            return False
    return True

def Player1Win (str1, str2):
    for i in range(len(str1)):
        if str1[i] > str2[i]:
            return True
        if str1[i] < str2[i]:
            return False


s = 0
for k in range(len(ar)):
    hand1 = ar[k][:14].split()
    hand2 = ar[k][15:][:-1].split()
    nhand1 = []
    for j in hand1:
        n = j[0]
        if n <= '9':
            nhand1.append(int(n))
        if n == 'T':
            nhand1.append(10)
        if n == 'J':
            nhand1.append(11)
        if n == 'Q':
            nhand1.append(12)
        if n == 'K':
            nhand1.append(13)
        if n == 'A':
            nhand1.append(14)
    nhand1.sort()
    nhand2 = []
    for j in hand2:
        n = j[0]
        if n <= '9':
            nhand2.append(int(n))
        if n == 'T':
            nhand2.append(10)
        if n == 'J':
            nhand2.append(11)
        if n == 'Q':
            nhand2.append(12)
        if n == 'K':
            nhand2.append(13)
        if n == 'A':
            nhand2.append(14)
    nhand2.sort()
    count1 = [nhand1.count(k) for k in nhand1]
    count2 = [nhand2.count(k) for k in nhand2]
    
    if checkStraight(nhand1):
        if checkFlush(hand1):
            strength1 = [9, nhand1[-1]]
            
        else:
            strength1 = [5, nhand1[-1]]
            
    elif checkFlush(hand1):
        strength1 = [6]
        for i in nhand1[::-1]:
            strength1.append(i)
        
    else:
        if count1.count(4) == 4:
            strength1 = [8]
            for i in nhand1:
                if nhand1.count(i) == 4:
                    strength1.append(i)
                    break
            for i in nhand1:
                if nhand1.count(i) == 1:
                    strength1.append(i)
                    break
            
        elif count1.count(3) == 3:
            if count1.count(2) == 2:
                strength1 = [7]
                for i in nhand1:
                    if nhand1.count(i) == 3:
                        strength1.append(i)
                        break
                for i in nhand1:
                    if nhand1.count(i) == 2:
                        strength1.append(i)
                        break
                
            else:
                strength1 = [4]
                for i in nhand1:
                    if nhand1.count(i) == 3:
                        strength1.append(i)
                        break
                while i in nhand1:
                    nhand1.remove(i)
                for i in nhand1[::-1]:
                    strength1.append(i)
                    
        elif count1.count(2) == 4:
            strength1 = [3]
            for i in nhand1[::-1]:
                if nhand1.count(i) == 2:
                    strength1.append(i)
                    break
            while i in nhand1:
                nhand1.remove(i)
            for i in nhand1:
                if nhand1.count(i) == 2:
                    strength1.append(i)
                    break
                
        elif count1.count(2) == 2:
            strength1 = [2]
            for i in nhand1:
                if nhand1.count(i) == 2:
                    strength1.append(i)
                    break
            while i in nhand1:
                nhand1.remove(i)
            for i in nhand1[::-1]:
                strength1.append(i)
            
        elif count1.count(1) == 5:
            strength1 = [1]
            for i in nhand1[::-1]:
                strength1.append(i)

    #

    if checkStraight(nhand2):
        if checkFlush(hand2):
            strength2 = [9, nhand2[-1]]
            
        else:
            strength2 = [5, nhand2[-1]]
            
    elif checkFlush(hand2):
        strength2 = [6]
        for i in nhand2[::-1]:
            strength2.append(i)
        
    else:
        if count2.count(4) == 4:
            strength2 = [8]
            for i in nhand2:
                if nhand2.count(i) == 4:
                    strength2.append(i)
                    break
            for i in nhand2:
                if nhand2.count(i) == 1:
                    strength2.append(i)
                    break
            
        elif count2.count(3) == 3:
            if count2.count(2) == 2:
                strength2 = [7]
                for i in nhand2:
                    if nhand2.count(i) == 3:
                        strength2.append(i)
                        break
                for i in nhand2:
                    if nhand2.count(i) == 2:
                        strength2.append(i)
                        break
                
            else:
                strength2 = [4]
                for i in nhand2:
                    if nhand2.count(i) == 3:
                        strength2.append(i)
                        break
                while i in nhand2:
                    nhand2.remove(i)
                for i in nhand2[::-1]:
                    strength2.append(i)
                    
        elif count2.count(2) == 4:
            strength2 = [3]
            for i in nhand2[::-1]:
                if nhand2.count(i) == 2:
                    strength2.append(i)
                    break
            while i in nhand2:
                nhand2.remove(i)
            for i in nhand2:
                if nhand2.count(i) == 2:
                    strength2.append(i)
                    break
                
        elif count2.count(2) == 2:
            strength2 = [2]
            for i in nhand2:
                if nhand2.count(i) == 2:
                    strength2.append(i)
                    break
            while i in nhand2:
                nhand2.remove(i)
            for i in nhand2[::-1]:
                strength2.append(i)
            
        elif count2.count(1) == 5:
            strength2 = [1]
            for i in nhand2[::-1]:
                strength2.append(i)

    s += Player1Win(strength1, strength2)
print(s)


if __name__ == '__main__':
    print(main())
