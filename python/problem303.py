import array


ANSWER = 1111981904675169
POWER = 4
LIMIT = 10 ** POWER


def main():
    lst = array.array('Q', (1, 2))
    st = set(range(1, LIMIT + 1))
    # important optimization, number for LIMIT - 1 is included in 'return' line
    st.discard(LIMIT - 1)
    total = 0
    while st:
        for k in st.copy():
            for n in lst:
                if not n % k:
                    st.discard(k)
                    total += n // k
                    break
        lst = array.array('Q', (n * 10 + i for n in lst for i in range(3)))
    return total + int('1' * POWER + '2' * POWER * 4) // (LIMIT - 1)


if __name__ == '__main__':
    print(main())
