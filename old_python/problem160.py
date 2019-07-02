LIMIT = 1000000000000

digits = 5
power = 10**digits
LIMIT = power * 2

f1 = f2 = 1
for i in range(1, 101):
    f1 *= i
    f2 *= i + 100
    print(f1)
    print(f2)
    print()
