import euler

def abun (n):
    return n < euler.sum_divisors(n)

lst  = [i for i in range(1, 28124) if abun(i)]
l = len(lst)
LIMIT = 28124 // 2
st = [i for i in range(28124 * 2)]
for i in range(l):
    ai = lst[i]
    if ai >= LIMIT:
        break
    for j in range(i, l):
        st[ai + lst[j]] = 0
print(sum(st[:28124]))
