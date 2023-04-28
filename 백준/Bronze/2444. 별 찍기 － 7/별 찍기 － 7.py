a = 5
a = int(input())
count = 1
b = a-1
while count < a:
    print(' '*b, '*'*(count*2-1), sep='')
    count += 1
    b -= 1
while count > 0:
    print(' '*b, '*'*(count*2-1), sep='')
    count -= 1
    b += 1
