import collections
import itertools

import euler


ANSWER = None
LIMIT = 4


def main():
    counts = collections.defaultdict(int)
    for c in itertools.count(1):
        for trio in euler.pythagorean_trio_my(c):
            for n in trio:
                counts[n] += 1
                if counts[n] == LIMIT:
                    return n
    return 0


if __name__ == '__main__':
    print(main())
