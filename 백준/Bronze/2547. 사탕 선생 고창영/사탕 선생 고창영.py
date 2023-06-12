from sys import stdin

input = stdin.readline
for _ in range(int(input())):
    input()
    candy_list = []
    N = int(input())
    for _ in range(N):
        candy_list.append(int(input().strip()))
    print("YES" if sum(candy_list) % N == 0 else "NO")