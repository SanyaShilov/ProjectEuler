lst = [1, 2]
st = {i for i in range(1, 10001)}
st.discard(9999)
s = 0
while st:
    for k in st.copy():
        for n in lst:
            if not n % k:
                st.discard(k)
                s += n//k
                break
    newar = []
    for k in lst:
        t = k*10
        newar.append(t)
        newar.append(t+1)
        newar.append(t+2)
    lst = newar
print(s+11112222222222222222//9999)


if __name__ == '__main__':
    print(main())
