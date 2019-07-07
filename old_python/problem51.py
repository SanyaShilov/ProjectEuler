import itertools
import sys
import euler

def all_masks (pr):
    result = []
    s = str(pr)
    for i in range(10):
        stri = str(i)
        c = s.count(stri)
        if c >= 3:
            st = set()
            for perm in itertools.permutations([True for i in range(3)]+
                                               [False for i in range(c - 3)]):
                st.add(perm)
            for perm in st:
                j = 0
                mask = ''
                for symbol in s:
                    if symbol == stri:
                        if perm[j]:
                            mask += '*'
                        else:
                            mask += stri
                        j += 1
                    else:
                        mask += symbol
                result.append(mask)
    return result    

length = 10000000
prime_list = euler.prime_list(length)
masks = {}
for pr in prime_list:
    for mask in all_masks(pr):
        if mask in masks:
            masks[mask] += 1
            if masks[mask] == 8:
                start = 0
                if mask.startswith('*'):
                    start = 1
                for i in range(start, 10):
                    n = int(mask.replace('*', str(i)))
                    if euler.is_prime(n, prime_list):
                        print(n)
                        sys.exit()
        else:
            masks[mask] = 1
