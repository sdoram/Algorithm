import sys
input = sys.stdin.readline
for _ in range(int(input())):
    num = input().rstrip()
    print('Do-it' if num[len(num)//2-1] == num[len(num)//2] else 'Do-it-Not')