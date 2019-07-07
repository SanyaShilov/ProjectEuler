ANSWER =


class point ():
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def middle (p1, p2):
        return point((p1.x+p2.x)/2, (p1.y+p2.y)/2)
    def length (p1, p2):
        return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5
    def sq(p1, p2, p3):
        a = point.length(p1, p2)
        b = point.length(p1, p3)
        c = point.length(p2, p3)
        half_per = (a+b+c)/2
        result = half_per*(half_per-a)*(half_per-b)*(half_per-c)
# из-за плавающих вычислений half_per может оказаться меньше одной из сторон
# на величину погрешности (когда точки на одной прямой)
        if result < 0:
            result = 0
        return result**0.5

lst = open('../txt/problem102.txt').readlines()
lst = [k.split(',') for k in lst]
lst = [[int(c) for c in k] for k in lst]
s = 0
p = point(0, 0)
for k in lst:
    p1, p2, p3 = point(k[0], k[1]), point(k[2], k[3]), point(k[4], k[5])
    if abs(point.sq(p1, p2, p3)-point.sq(p1, p2, p)-point.sq(p1, p3, p)-
           point.sq(p2, p3, p)) < 1e-5:
        s += 1
print(s)


if __name__ == '__main__':
    print(main())
