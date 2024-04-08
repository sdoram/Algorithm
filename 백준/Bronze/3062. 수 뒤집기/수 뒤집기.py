import sys
input = sys.stdin.readline
for _ in range(int(input())):
    NUM = input()
    TOTAL_NUM = str(int(NUM) + int(NUM[::-1]))
    COUNT = 0
    for N, T in enumerate(TOTAL_NUM[::-1]):
        if T != TOTAL_NUM[N]:
            COUNT -= 1
            break
    print('YES' if COUNT == 0 else 'NO')