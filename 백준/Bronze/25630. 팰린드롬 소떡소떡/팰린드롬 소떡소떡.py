import sys
input = sys.stdin.readline
N = int(input())
beef_rice_cake = input().rstrip()

print(sum([1 if beef_rice_cake[i] != n else 0 for i, n in 
                enumerate(beef_rice_cake[:N // 2 - 1 if N % 2 == 0 else N // 2:-1])]))