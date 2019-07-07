ANSWER =


lst = [(100003 - 200003*i + 300007*i*i*i)%1000000 - 500000 for i in range(56)]
print(lst[10])

for i in range(100-55):
    lst.append((lst[-24]+lst[-55]) % 1000000 - 500000)

print(lst[100])

leng = 4


if __name__ == '__main__':
    print(main())
