ANSWER =


b = bin(10**25)[2:]

def calc (b):
    l = len(b)
    rf = b.rfind('1')
    if b.count('1') == 1:
        return l-rf
    return calc(b[:rf])+(l-rf-1)*calc(b[:rf]+'0')

print(calc(b))


if __name__ == '__main__':
    print(main())
