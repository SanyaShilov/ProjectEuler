ANSWER = 1582
LIMIT = 200


def main():
    lst = [[], [{1}]]
    for i in range(2, LIMIT + 1):
        lst.append([])
        for j in range(i // 2, i):
            d = i - j
            for st in lst[j]:
                if d in st:
                    lst[-1].append(st.union({i}))
        minimum_len = len(min(lst[-1], key=len))
        lst[-1] = [st for st in lst[-1] if len(st) == minimum_len]
    return sum(len(lst[i][0]) - 1 for i in range(1, LIMIT + 1))


if __name__ == '__main__':
    print(main())
