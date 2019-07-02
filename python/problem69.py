import euler


ANSWER =


totient = euler.totientlist(1000000+1)
lst = [0]+[i/totient[i] for i in range(1, 1000000+1)]
print(lst.index(max(lst)))


if __name__ == '__main__':
    print(main())
