import primes
import math
primelist = primes.prime_list(190)
big = 1
for pr in primelist :
    big *= pr
sqrt = 2323218950681478446587180516177954548
'''
arnum = [sq]
arprod = [1]
arind = [-1]
res = 0
while arnum :
    num = arnum.pop()
    prod = arprod.pop()
    ind = arind.pop()
    if num < res :
        continue
    for i in range(ind+1, 42) :
        product = prod*primelist[i]
        n = num - num%product
        if n > res :
                arnum.append(n)
                arprod.append(product)
                arind.append(i)
                if not big % n :
                    print('res', n, len(arnum))
                    res = n
'''
numbers = [sqrt]
products = [1]
indices = [-1]
result = 0
while numbers :
    number = numbers.pop()
    product = products.pop()
    index = indices.pop()
    if number < result : # a little bit faster with this 'if'
        continue
    for i in range(index+1, 42) :
        newproduct = product*primelist[i]
        newnumber = number - number%newproduct # find a newnumber <= number, that is divisible by previous product and new prime.     
        if newnumber > result : # not interested in numbers less than the result we already have
                numbers.append(newnumber)
                products.append(newproduct)
                indices.append(i)
                if not big % newnumber : # it can be the right answer!
                    result = newnumber
                    print('result', result) # the 7th printed number is the right answer
