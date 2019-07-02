ar = [(100003 - 200003*i + 300007*i*i*i)%1000000 - 500000 for i in range(56)]
print(ar[10])

for i in range(100-55):
    ar.append((ar[-24]+ar[-55]) % 1000000 - 500000)

print(ar[100])

leng = 4
