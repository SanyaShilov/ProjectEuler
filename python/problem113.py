ANSWER =


N = 100

increasing = [[1] for i in range(9)]

for i in range(1, N):
    for j in range(9):
        increasing[j].append(sum(increasing[n][i-1] for n in range(j, 9)))



decreasing = [[1] for i in range(9)]

for i in range(1, N):
    for j in range(9):
        decreasing[j].append(1+sum(decreasing[n][i-1] for n in range(j+1)))

s = 0
for k in increasing:
    s += sum(k)
for k in decreasing:
    s += sum(k)
s -= 9*N
print(s)


if __name__ == '__main__':
    print(main())
