import euler

def max_deLIMITer (n):
    i = 0
    pr = prime_list[0]
    sq = (n+1)**0.5
    while pr < sq:
        if n % pr == 0:
            n //= pr
            sq = (n+1)**0.5
            i -= 1
        i += 1
        pr = prime_list[i]
    return n

def calc (n):
    nn = n+1
    i = 0
    pr = prime_list[0]
    sq = (nn+1)**0.5
    while pr < sq:
        if nn % pr == 0:
            nn = nn//pr
            sq = (nn+1)**0.5
            i = -1
        i += 1
        pr = prime_list[i]
    return nn-1

def calc (n):
    return max_deLIMITer(n+1)

def cubcalc (n):
    num = n*n-n+1
    m = max_deLIMITer(num)
    mn = max_deLIMITer(n+1)
    if m > mn:
        return m - 1
    return mn - 1

l = 10000
prime_list = euler.prime_list(l+10)

s = 0
for i in range(1, l + 1):
    c = cubcalc(i)
    s += c
print(s)

'''
n = 1;
S = 0;
num = n*n - n + 1;
fm = FactorInteger[num];
m = Max[fm[[{-1}, 1]]];
While[n <= 2 * 10^6,
	num = n*n - n + 1;
	fm = FactorInteger[num];
	m = Max[fm[[{-1}, 1]]];
	fmn = FactorInteger[n + 1];
	mn = Max[fmn[[{-1}, 1]]];
	If[m > mn, S += m - 1, S += n];
	n += 1;
];
S
'''

n = 1
s = 0
while n <= l:
    num = n*n - n + 1
    m = max_deLIMITer(num)
    mn = max_deLIMITer(n+1)
    s += max(m, mn) - 1
    n += 1
print(s)
# 269533519465604486 is not correct


if __name__ == '__main__':
    print(main())
