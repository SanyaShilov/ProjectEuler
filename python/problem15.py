ANSWER =


fact = [1]
for i in range(1, 50):
    fact.append(fact[-1]*i)

print(fact[40]//fact[20]//fact[20])


if __name__ == '__main__':
    print(main())
