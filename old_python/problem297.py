F = [1, 2]
for i in range(100):
    F.append(F[-1]+F[-2])
    if F[-1] > 10**6:
        break
print(F)
S = [1, 1, 3]
for i in range(len(F)-4):
    S.append(S[-1]+S[-2]+F[i])
print(S)
print(sum(S))


def Zeckendorf (n):
    if n < 5:
        return n-1
    F = [1, 2]
    while F[-1] < n:
        F.append(F[-1]+F[-2])
    S = [1, 1, 3]
    for i in range(len(F)-4):
        S.append(S[-1]+S[-2]+F[i])
    if F[-1] == n:
        return sum(S)
    r = n - F[-2]
    return sum(S[:-1])+r+Zeckendorf(r)
