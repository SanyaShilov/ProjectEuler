import itertools


ANSWER = None


def main():
    total = 0
    for comb in itertools.product(range(10), repeat=8):
        grid_sum = sum(comb[:4])
        e = grid_sum - comb[0] - comb[4] - comb[6]
        g = grid_sum - comb[2] - comb[5] - comb[7]
        f = grid_sum - comb[3] - comb[5] - e
        h = grid_sum - comb[6] - comb[7] - f
        b = (grid_sum - comb[4] - comb[5] - comb[3] - h + comb[0] + comb[7]) / 2
        if not b.is_integer():
            continue
        b = round(b)
        a = grid_sum - comb[4] - comb[5] - b
        c = grid_sum - comb[1] - a - f
        d = grid_sum - comb[3] - b - h
        for n in (e, f, g, h, a, b, c, d):
            if n < 0 or n > 9:
                break
        else:
            total += 1
    return total


if __name__ == '__main__':
    print(main())
