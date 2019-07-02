import euler
import array

prime_list = euler.prime_list(1000000)

ar = array.array('L', (0 for i in range(10000000)))

for pr in prime_list:
    ar[pr] = 1

s = 0
for i in range(1, 600):
    pr = 3*i*i-3*i+1
    if ar[pr]:
        s += 1
print(s)


if __name__ == '__main__':
    print(main())
