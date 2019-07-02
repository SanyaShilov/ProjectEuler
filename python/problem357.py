#
import array

def prime_list (n):
    index = array.array('L', (1 for i in range(n)))
    
    i = 2
    while i < n:
        if index[i]:
            j = i+i
            while j < n:
                index[j] = 0
                j += i
        i += 1
    index[0] = index[1] = 0
    return index

def check (n):
    sqrt = int(n**0.5)+2
    for i in range(1, LIMIT):
        if i > sqrt:
            break
        if not n % i:
            if not prime_list[i+n//i]:
                return False
    return True

st = []
LIMIT = 100*1000000+2
prime_list = prime_list(LIMIT)
prime_list += array.array('L', (0 for i in range(1000)))
sq = [p*p for p in range(int(len(prime_list)**0.5)+1) if prime_list[p]]
for i in range(2, LIMIT-1):
    q = 2*i-4
    if q >= LIMIT:
        break
    if prime_list[i]:
        if prime_list[q+1]:
            yes = True
            for s in sq:
                if s > q:
                    break
                if not q % s:
                    yes = False
                    break
            if yes:
                st.append(q)
st2 = []
for p in st:
    if check(p):
        st2.append(p)
print(sum(st2)+1)


if __name__ == '__main__':
    print(main())
