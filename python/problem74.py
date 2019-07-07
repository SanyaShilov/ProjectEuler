ANSWER =


def fact (n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

fact_table = [fact(n) for n in range(10)]

def get_next (n):
    result = 0
    while n:
        result += fact_table[n % 10]
        n //= 10
    return result

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
    result = get_chain(get_next(n))+1
    chain[n] = result
    return result

number = 0

for i in range(3, 1000000):
    c = get_chain(i)
    if c == 60:
        number += 1
print(number)


if __name__ == '__main__':
    print(main())
