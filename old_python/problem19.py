months = [31,
          28,
          31,
          30,
          31,
          30,
          31,
          31,
          30,
          31,
          30,
          31]

def is_leap (year):
    if year % 4:
        return False
    if year % 25:
        return True
    if year % 16:
        return False
    return True

temp = 1
year = 1901
mon = 0
res = 0

while year != 2001:
    if is_leap(year):
        months[1] = 29
    else:
        months[1] = 28
    for i in range(12):
        temp = (temp+months[i])%7
        if temp == 6:
            res += 1
    year += 1
print(res)
