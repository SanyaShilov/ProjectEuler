import euler
for a in range(int((1000//2)**0.5)):
    for trio in euler.pythagorean_trio(a):
        if sum(trio) == 1000:
            print(trio[0]*trio[1]*trio[2])
            break
