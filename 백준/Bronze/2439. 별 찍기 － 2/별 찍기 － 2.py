a = int(input())
count = 0
while a > count:
    count += 1
    star = count * '*'
    print(star.rjust(a))
