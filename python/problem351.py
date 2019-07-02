import euler

LIMIT = 10**8

eul = euler.totientlist(LIMIT+1)

r = (LIMIT*(LIMIT+1)//2-sum(eul))*6
print(r)


if __name__ == '__main__':
    print(main())
