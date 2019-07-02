ANSWER =


coins = [1, 2, 5, 10, 20, 50, 100, 200]
s = 0

def work (sum, index):
    global s
    if sum == 200:
        s += 1
    else:
        for i in range(index, 8):
            ss = sum + coins[i]
            if ss > 200:
                break
            work(ss, i)

work(0, 0)
print(s)


if __name__ == '__main__':
    print(main())
