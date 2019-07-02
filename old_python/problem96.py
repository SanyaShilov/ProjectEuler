import copy

f = open('../txt/problem096.txt')
read = f.readlines()

r = range(9)

def load (number, read):
    temp = read[number*10+1:(number+1)*10]
    m = []
    for l in temp:
        m.append([])
        for i in l:
            try:
                m[-1].append(int(i))
            except:
                pass
        
    return m

def Solved (m):
    for i in r:
        for j in r:
            if m[i][j] == 0:
                return False
    return True

def SolveN (n, canbe, m):
    solved = 0
    
    for i in r:
        ind = -1
        for j in r:
            if canbe[i][j]:
                if ind == -1:
                    ind = j
                else:
                    ind = -2
        if ind > -1:
            solved += 1
            m[i][ind] = n

    for i in r:
        ind = -1
        for j in r:
            if canbe[j][i]:
                if ind == -1:
                    ind = j
                else:
                    ind = -2
        if ind > -1:
            solved += 1
            m[ind][i] = n
    
    for isq in range(3):
        for jsq in range(3):
            indi = -1
            indj = -1
            for i in range(3*isq, 3*isq + 3):
                for j in range(3*jsq, 3*jsq + 3):
                    if canbe[i][j]:
                        if indi == -1:
                            indi = i
                            indj = j
                        else:
                            indi = -2
            if indi > -1:
                solved += 1
                m[indi][indj] = n
                
    return solved

def Deduct (m):
    solved = 0
    
    ar = [WhereCanBe(i, m) for i in range(1, 10)]
    for i in r:
        for j in r:
            num = -1
            for nn in r:
                if ar[nn][i][j]:
                    if num == -1:
                        num = nn+1
                    else:
                        num = -2
            if num > -1:
                m[i][j] = num
                solved += 1
                
    return solved

def Guess (m, n):
    can = WhereCanBe(n, m)
    for i in r:
        for j in r:
            if can[i][j]:
                m[i][j] = n
                return (True, i, j)
    return (False, -1, -1)

def Solve (m, guessed = False):
    while not Solved(m):
        s = 0
        for i in range(1, 10):
            can = WhereCanBe(i, m)
            s += SolveN(i, can, m)
        if s == 0:
            s += Deduct(m)
        if s == 0:
            
            if guessed:
                return (False, m)
        
            for i in range(1, 10):
                cm = copy.deepcopy(m)
                g = Guess(cm, i)
                if g:
                    S = Solve(cm, guessed = True)
                    if S[0]:
                        m = cm
                        return (True, m)
            return (False, m)
                    
    return (True, m)

def Solve (m):
    while not Solved(m):
        s = 0
        for i in range(1, 10):
            can = WhereCanBe(i, m)
            s += SolveN(i, can, m)
        if s == 0:
            s += Deduct(m)
        if s == 0:
            
            for i in range(1, 10):
                cm = copy.deepcopy(m)
                g = Guess(cm, i)
                
                if g[0]:
                    S = Solve(cm)
                    if Correct(S[1]):
                        m = copy.deepcopy(S[1])
                        break
            break

    if Correct(m):
        return (True, m)
    return (False, m)

def Empty (m):
    return [[1 if m[i][j] == 0 else 0 for j in r ] for i in r]

def WhereCanBe (n, m):
    nm = Empty(m)
    
    for i in r:
        for j in r:
            if m[i][j] == n:
                for k in r:
                    nm[i][k] = 0
                    nm[k][j] = 0
                for k in range(3*(i//3), 3*(i//3 + 1)):
                    for q in range(3*(j//3), 3*(j//3 + 1)):
                        nm[k][q] = 0
    
    return nm

def InSquare (n, m, row, col):
    for i in range(3*row, 3*row+3):
        for j in range(3*col, 3*col+3):
            if m[i][j] == n:
                return True
    return False

def Correct (m):
    for i in r:
        for n in range(1, 10):
            c = 0
            for j in r:
                if m[i][j] == n:
                    c += 1
            if c != 1:
                return False

    for i in r:
        for n in range(1, 10):
            c = 0
            for j in r:
                if m[j][i] == n:
                    c += 1
            if c != 1:
                return False
            
    return True

res = 0
for n in range(50):
    m = load(n, read)
    s = Solve(m)
    res += 100*s[1][0][0] + 10*s[1][0][1] + s[1][0][2]
print(res)
