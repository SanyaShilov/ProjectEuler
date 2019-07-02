# DYNAMIC PROGRAMMING

def comb3 (m, n): # сочетания без повторений (выбрать m из n предметов без учета порядка)
    return [] if m < 0 else [[]] if m == 0 else [c+[i] for c in comb3(m-1, n) for i in range(n) if i > max(c+[-1])]

def choose (lst):
    return [[lst[:i]+lst[i+1:], lst[i]] for i in range(len(lst))]

tab =  [[7,  53, 183, 439, 863],
        [497, 383, 563,  79, 973],
        [287,  63, 343, 169, 583],
        [627, 343, 773, 959, 943],
        [767, 473, 103, 699, 303]]

tab = open('p345.txt').readlines()
tab = [k.split() for k in tab]
tab = [[int(c) for c in k] for k in tab]

leng = len(tab)

solve = [[] for k in range(leng)]

solve[0] = [[[i], tab[0][i]] for i in range(leng)]

for i in range(1, leng):
    c = comb3(i+1, leng)
    solve[i] = [[c[j], 0] for j in range(len(c))]

for i in range(1, leng):
    li = len(solve[i])
    last = [k[0] for k in solve[i-1]]
    for j in range(li):
        ch = choose(solve[i][j][0])
        ind = [last.index(k[0]) for k in ch]
        l = len(ind)
        solve[i][j][1] = max(solve[i-1][ind[k]][1] + tab[i][ch[k][1]] for k in range(l))
        
print(solve[leng-1][0][1])



if __name__ == '__main__':
    print(main())
