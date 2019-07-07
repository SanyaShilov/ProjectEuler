ones = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    ]

tens = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
    ]

bigtens = [
    '',
    '',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
    ]

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

def count (i):
    result = 0
    if (i // 100) and (i % 100):
        result += len('and')
    
    r = i // 100
    if r:
        result += len(ones[r])+len('hundred')

    r = (i // 10) % 10
    if r:
        if r == 1:
            r2 = i % 10
            result += len(tens[r2])
            return result
        else:
            result += len(bigtens[r])

    r2 = i % 10
    if r2:
        result += len(ones[r2])
    return result


result = len('onethousand')
for i in range(1, 1000):
    result += count(i)
print(result)
