import euler

prime_list = euler.prime_list(1000)



def semidiv (n, a, b):
    if n % a:
        return not n % b
    return n % b

i1 = 0
i2 = 0
pr1 = prime_list[i1]
pr2 = prime_list[i2]
s = 0
for i in range(4, 1000):
    sq = i**0.5
    pr1n = prime_list[i1+1]
    if pr1n <= sq:
        pr1 = pr1n
        i1 += 1
    if pr2 < sq:
        i2 += 1
        pr2 = prime_list[i2]
    if semidiv(i, pr1, pr2):
        s += i
print(s)
