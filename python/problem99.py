ANSWER =


lst = open('../txt/problem099.txt').readlines()
lst = [k.split(',') for k in lst]
lst = [[int(k[0]), int(k[1])/10000] for k in lst]
result = [k[0]**k[1] for k in lst]
print(result.index(max(result))+1)


if __name__ == '__main__':
    print(main())
