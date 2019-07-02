s = ''
for i in range(0, 250000):
    s += str(i)
a = int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * \
int(s[100000]) * int(s[1000000])
print(a)
