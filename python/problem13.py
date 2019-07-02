ANSWER =


print(str(sum((int(l.split()[0]) for l in open('../txt/problem013.txt').readlines())))[:10])


if __name__ == '__main__':
    print(main())
