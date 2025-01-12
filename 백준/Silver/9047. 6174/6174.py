import sys

input = sys.stdin.readline

for _ in range(int(input())):
    num = int(input())
    re_num = list(str(num))
    count = 0
    while True:
        if num == 6174:
            break
        num = int(''.join(sorted(re_num, reverse=True))) - int(''.join(sorted(re_num)))
        re_num = list(str(num) + (4 - len(str(num))) * '0') if len(str(num)) != 4 else list(str(num))
        count += 1
    print(count)