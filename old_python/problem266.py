import euler

prime_list = euler.prime_list(190)
big = 1
for pr in prime_list:
    big *= pr
sqrt = euler.int_sqrt(big)

print(sqrt)
print()

result = 0
def work (number, product, index):
    global result
    if number < result:
        pass
    for i in range(42 - 1, index, -1):
        newproduct = product*prime_list[i]
        newnumber = number - number%newproduct # find a newnumber <= number, that is divisible by previous product and new prime.     
        if newnumber > result: # not interested in numbers less than the result we already have
            if not big % newnumber: # it can be the right answer!
                result = newnumber
                print(result) # the 7th printed number is the right answer
            work(newnumber, newproduct, i)
            
work(sqrt, 1, -1)

'''
result 2323218567708983222604250026334804230
result 2323218590899448529000677546735762759
result 2323218947021562122734557024235572863
result 2323218950606397230212274067850235355
result 2323218950647167552155094528537222119
result 2323218950654637851620301685771301719
result 2323218950659046189161096883702440585
'''
