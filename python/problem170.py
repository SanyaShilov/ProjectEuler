ANSWER =


digits = '0123456789'

def form_next_pandigitals (last):
    for n in last:
        for d in digits:
            if d not in n:
                yield n + d

last = [d for d in digits if d != '0']
al = []
al.extend(last)
for i in range(9):
    nxt = list(form_next_pandigitals(last))
    print(len(nxt))
    last = nxt
    al.extend(nxt)
ial = [int(a) for a in al]


if __name__ == '__main__':
    print(main())
