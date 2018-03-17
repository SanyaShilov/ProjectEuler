def is_pr (d1, d2, d3) :
    s = d1 + d2 + d3
    if abs(s-2*d1) < 1e-5 :
        return True
    if abs(s-2*d2) < 1e-5 :
        return True
    if abs(s-2*d3) < 1e-5 :
        return True
    return False

dist = [[x**2+y**2 for y in range(51)] for x in range(51)]
dist2 = [[[[(x1-x2)**2+(y1-y2)**2 for y2 in range(51)] for x2 in range(51)]
          for y1 in range(51)] for x1 in range(51)]
s = 0
for x1 in range(51) :
    for y1 in range(51) :
        if x1 + y1 != 0 :
            for x2 in range(51) :
                for y2 in range(51) :
                    if x2 + y2 != 0 :
                        if x1 != x2 or y1 != y2 :
                            if is_pr(dist[x1][y1], dist[x2][y2], dist2[x1][y1][x2][y2]) :
                                s += 1
print(s//2)












