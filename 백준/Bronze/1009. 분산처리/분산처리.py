import sys
T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a1, b1 = int(str(a)[-1]), int(str(b)[-2:])
    total_num = str(a1 ** b1)
    if int(total_num[-1]) == 0:
        print(10)
    else:
        print(int(total_num[-1]))