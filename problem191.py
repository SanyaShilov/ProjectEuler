# Late # consecutive Absent

ar = [[0, 0, 1], #0 
      [0, 1, 1], #1
      [0, 2, 0], #2
      [1, 0, 1], #3
      [1, 1, 0], #4
      [1, 2, 0]] #5

def iteration (ar) :
    newar =  [[0, 0, 0],
              [0, 1, 0],
              [0, 2, 0],
              [1, 0, 0],
              [1, 1, 0],
              [1, 2, 0]]
    '''
    for k in ar[:] :
        if k[0] :
            newar.append([1, 0]) # On time
            if k[1] != 2 :
                newar.append([1, k[1]+1]) # Absent
        else :
            newar.append([1, 0]) # Late
            newar.append([0, 0]) # On time
            if k[1] != 2 :
                newar.append([0, k[1]+1]) # Absent

        '''
    for k in ar :
        num = k[2]
        if k[0] :
            newar[3][2] += num # On time
            if k[1] == 0 :
                newar[4][2] += num # Absent
            if k[1] == 1 :
                newar[5][2] += num # Absent
        else :
            newar[0][2] += num # On time
            newar[3][2] += num # Late
            if k[1] == 0 :
                newar[1][2] += num # Absent
            if k[1] == 1 :
                newar[2][2] += num # Absent
    return newar

for i in range(29) :
    print(i)
    ar = iteration(ar)
s = 0
for k in ar :
    s += k[2]
print(s)
