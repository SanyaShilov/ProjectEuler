a = 1
for i in range(7830457) :
    a *= 2
    a = a % 10**10
a = a * 28433 + 1
print(a % 10**10)
