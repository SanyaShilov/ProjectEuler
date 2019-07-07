ANSWER =


lst = open('../txt/problem042.txt').readlines()
lst = lst[0][1:-1].split('\",\"')
tr = [k*(k+1)//2 for k in range(1, 50)]
def value (w):
    s = 0
    for i in range(len(w)):
        s += ord(w[i])
        s -= 64
    return s
num = 0
for k in lst:
    if value(k) in tr:
        num += 1
print(num)


if __name__ == '__main__':
    print(main())
