import sys
while True:
    one, two = sys.stdin.readline().split()
    count = 0
    if one == '0' and two == '0':
        break
    elif int(one) > int(two):
        two = two.zfill(len(one))
    else:
        one = one.zfill(len(two))
    for n, i in enumerate(range(len(one))[::-1], 1):
        count += 1 if int(one[i:]) + int(two[i:]) >= (2*5)**n else 0
    print(count)