import sys
for _ in range(3):
    sum_num = 0
    N = int(sys.stdin.readline())
    for _ in range(N):
        sum_num += int(sys.stdin.readline())
    if sum_num > 0:
        print('+')
    elif sum_num == 0:
        print('0')
    else:
        print('-')