s = 0
st = set()
for i in range(1, 100000) :
    if not i % 32 :
        if i % 5 :
            s += 1
            st.add(i)
print(s)
