import itertools


ANSWER = 2009
LIMIT = 124


def main():
    index = 1
    for i in itertools.count(3, 2):
        remainders = (1, 1, 1)
        st = {remainders}
        while remainders[-1]:
            remainders = remainders[1:] + (sum(remainders) % i,)
            if remainders in st:
                if index == 124:
                    return i
                index += 1
                break
            st.add(remainders)


if __name__ == '__main__':
    print(main())
