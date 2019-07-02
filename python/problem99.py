ANSWER =


ar = open('../txt/problem099.txt').readlines()
ar = [k.split(',') for k in ar]
arr = [[int(k[0]), int(k[1])/10000] for k in ar]
res = [k[0]**k[1] for k in arr]
print(res.index(max(res))+1)


if __name__ == '__main__':
    print(main())
