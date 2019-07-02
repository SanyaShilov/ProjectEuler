ANSWER =


def fact (n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

fact_table = [fact(n) for n in range(10)]

def get_next (n):
    res = 0
    while n:
        res += fact_table[n % 10]
        n //= 10
    return res

chain = [0 for i in range(10000000)]
chain[1] = 1
chain[2] = 1
chain[145] = 1
chain[40585] = 1
chain[169] = chain[363601] = chain[1454] = 3
chain[871] = chain[45361] = 2
chain[872] = chain[45362] = 2

def get_chain (n):
    if chain[n]:
        return chain[n]
    res = get_chain(get_next(n))+1
    chain[n] = res
    return res

number = 0

for i in range(3, 1000000):
    c = get_chain(i)
    if c == 60:
        number += 1
print(number)


if __name__ == '__main__':
    print(main())
