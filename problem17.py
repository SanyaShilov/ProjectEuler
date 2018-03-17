ones = ['zero',
        'one',
         'two',
         'three',
         'four',
         'five',
         'six',
         'seven',
         'eight',
         'nine']

tens = ['ten',
         'eleven',
         'twelve',
         'thirteen',
         'fourteen',
         'fifteen',
         'sixteen',
         'seventeen',
         'eighteen',
         'nineteen']

bigtens = ['zero',
           'zero',
            'twenty',
             'thirty',
             'forty',
             'fifty',
             'sixty',
             'seventy',
             'eighty',
             'ninety']

# one
# two
# three
# four
# five
# six
# seven
# eight
# nine
# ten
# eleven
# twelve
# thirteen
# fourteen
# fifteen
# sixteen
# seventeen
# eighteen
# nineteen
# twenty
# thirty
# forty
# fifty
# sixty
# seventy
# eighty
# ninety
# hundred
# one thousand

res = len('onethousand')

def count (i) :
    res = 0
    if (i // 100) and (i % 100) :
        res += len('and')
    
    r = i // 100
    if r :
        res += len(ones[r])+len('hundred')

    r = (i // 10) % 10
    if r :
        if r == 1 :
            r2 = i % 10
            res += len(tens[r2])
            return res
        else :
            res += len(bigtens[r])

    r2 = i % 10
    if r2 :
        res += len(ones[r2])
    return res


res = len('onethousand')
for i in range(1, 1000) :
    res += count(i)
print(res)
