#
s = set()
n = 10**12
for base in range(2, int(n**0.5)+1) :
    last = base*base
    num = last + base + 1
    while num < n :
        s.add(num)
        last *= base
        num += last
print(sum(s)+1)
