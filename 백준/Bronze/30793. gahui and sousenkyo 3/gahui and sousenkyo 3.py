x, y = map(int, input().split())
if x / y < 0.2:
    print('weak')
elif x / y < 0.4:
    print('normal')
elif x / y < 0.6:
    print('strong')
else:
    print('very strong')