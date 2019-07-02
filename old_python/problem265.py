'''
str1 = '1'*5+'2'*5+'1'+'0'*20+'2'
print(str1, str1.count('0'))
ar = [str1]
str2 = '1'*5+'2'+'0'*20+'1'+'2'*5
print(str2, str2.count('0'))
st = '1'*5+'2'
for i in range(25-7+1):
    stt = st+'0'*i+'1222221'+'0'*(18-i)+'2'
    print(stt, stt.count('0'))

'''

'''
str1 = '1'*5+'2'+'0'*25+'2'

ar = [str1]
insert = ['1222221', '22212', '11121', '22211', '11122', '22122', '11211',
          '22121', '11212', '22112', '11221', '22111', '11222', '21222', '12111',
          '21221', '12112', '21212', '12121', '21211', '12122', '21122', '12211',
          '21121', '12212', '21112', '12221']

n = 0
for s in insert:
    ls = len(s)
    newar = []
    for st in ar:
        for i in range(32):
            for j in range(ls):
                if st[(i+j)%32] != '0' and st[(i+j)%32] != s[j]:
                    break
            else:
                newar.append((st[:i]+s+st[i+ls:])[:32])
    ar = newar
    n += 1

s = 0
for k in ar:
    st = ''
    for l in k:
        st += chr(ord(l)-1)
    s += int(st, 2)
print(s)
'''
# фантастика:


def f(n, s):
    if len(s) == 2**n + n-1: return int(s[:2**n], 2)
    return sum([f(n, s+d) for d in "01" if (s+d)[-n:] not in s])

print(f(5, "0"*5))

