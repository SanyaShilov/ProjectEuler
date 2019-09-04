import math


ANSWER = 259679


def shortest_edge(lst):
    shortest = math.inf
    shortest_i = -1
    shortest_j = -1
    r = range(len(lst))
    for i in r:
        for j in r:
            length = lst[i][j]
            if length and length < shortest:
                shortest = length
                shortest_i = i
                shortest_j = j
    return shortest_i, shortest_j


def connect(lst, st):
    shortest = math.inf
    shortest_i = -1
    shortest_j = -1
    for i in st:
        for j in range(len(lst)):
            if j not in st:
                length = lst[i][j]
                if length and length < shortest:
                    shortest = length
                    shortest_i = i
                    shortest_j = j
    st.add(shortest_j)
    return lst[shortest_i][shortest_j]


def main():
    lst = [
        [0 if n == '-' else int(n) for n in line[:-1].split(',')]
        for line in open('../txt/problem107.txt')
    ]
    leng = len(lst)
    i, j = shortest_edge(lst)
    st = {i, j}
    minimal = lst[i][j]
    for i in range(leng - 2):
        minimal += connect(lst, st)
    initial = sum(lst[i][j] for i in range(leng) for j in range(leng)) // 2
    return initial - minimal


if __name__ == '__main__':
    print(main())
