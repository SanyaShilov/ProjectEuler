# pylint: disable = invalid-name

ANSWER = 518408346


def brute_force():
    total = 0
    for n in range(4, 10 ** 9 // 3 + 3, 2):
        p1, p2 = 3 * n + 2, 3 * n - 2
        c1, c2 = p1 * (n + 2), p2 * (n - 2)
        if c1 == round(c1 ** 0.5) ** 2:
            total += p1
        if c2 == round(c2 ** 0.5) ** 2:
            total += p2
    return total
    # 518408346, about 10 minutes


def brute_force_2():
    total = 0
    for z in range(1, int(10 ** 9 / 16.392)):
        if z % 100000 == 0:
            print(z)
        z28 = (z * z) << 3
        z2plus = (z << 1) + 1
        x1 = (-z2plus + ((z2plus * z2plus) + z28) ** 0.5) / 2
        if x1.is_integer():
            p1 = round(6 * x1 + 12 * z + 2)
            total += p1
        else:
            z2minus = (z << 1) - 1
            x2 = (-z2minus + ((z2minus * z2minus) + z28) ** 0.5) / 2
            if x2.is_integer():
                p2 = round(6 * x2 + 12 * z - 2)
                total += p2
    return total
    # 518408346, about 5 minutes


def main():
    return brute_force_2()


if __name__ == '__main__':
    print(main())
