ANSWER = None


def main():
    for n in range(2 ** 6):
        binary = '{0:{fill}6b}'.format(n, fill='0')
        a, b, c = (int(n) for n in binary[:3])
        shift = binary[1:] + str(a ^ (b and c))
        if binary == shift:
            print('!!!!!!', binary)
        print(binary, shift)
    return 0


if __name__ == '__main__':
    print(main())
