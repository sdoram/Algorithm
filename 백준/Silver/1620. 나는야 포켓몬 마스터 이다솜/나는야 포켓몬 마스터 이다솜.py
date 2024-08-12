import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num_dict = {i:input().rstrip() for i in range(1, N+1)}
name_dict = {value: key for key, value in num_dict.items()}

for _ in range(M):
    T = input().rstrip()
    if T.isdigit():
        print(num_dict[int(T)])
    else:
        print(name_dict[T])