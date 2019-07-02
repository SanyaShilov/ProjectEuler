import string
import itertools


ANSWER =


ar = open('../txt/problem059.txt').readlines()
ar = ar[0].split(',')
ar = [int(k) for k in ar]

def decrypt (ar, key):
    artext = []
    i = 0
    l = len(key)
    for n in ar:
        artext.append(chr(n ^ key[i]))
        i += 1
        if i == l:
            i = 0
    return ''.join(artext)

def isword (s):
    for symbol in s:
        if symbol not in string.ascii_letters:
            return False
    return True

spaces = len(ar) // 10
symbols = string.printable
keyset = [ord(s) for s in string.ascii_lowercase]
for key in itertools.product(keyset, repeat = 3):
    text = decrypt(ar, key)
    
    if text.count(' ') < spaces:
        continue

    words = text.split()
    count = sum(isword(s) for s in words)
    if count < len(words)//2:
        continue

    if 'the' not in words or 'The' not in words:
        continue
    
    for s in text:
        if s not in symbols:
            break
    else:
        print(sum(ord(s) for s in text))


if __name__ == '__main__':
    print(main())
