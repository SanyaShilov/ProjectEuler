def abun (n) :
    d = 0
    for i in range(2, int(n**0.5)+1) :
        if n % i == 0 :
            d += i
            if n != i ** 2 :
                d += n // i
            if d > n :
                return True
    return False


ar  = [i for i in range(28123) if abun(i)]
print('ar')
st = set((i for i in range(28124)))
for i in ar :
    for j in ar :
        st.discard(i+j)
print(sum(st))
