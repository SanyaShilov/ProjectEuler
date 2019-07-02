import euler

def abun (n):
    return n < euler.sum_divisors(n)

ar  = [i for i in range(1, 28124) if abun(i)]
l = len(ar)
LIMIT = 28124 // 2
st = [i for i in range(28124 * 2)]
for i in range(l):
    ai = ar[i]
    if ai >= LIMIT:
        break
    for j in range(i, l):
        st[ai + ar[j]] = 0
print(sum(st[:28124]))
