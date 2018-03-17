mas = [i for i in range(100)]
for i in range(2, 101) :
    for j in range(2, 101) :
        try :
            mas[i*j] = 0
        except :
            pass
mas = [i for i in mas if i]
print(mas, len(mas))

ar = mas[:]
last_len = 4
while True :
    mas = {i*j for i in mas for j in ar if i*j <= 1000000000}
    l = len(mas)
    if l == last_len :
        break
    last_len = l
print(l)
