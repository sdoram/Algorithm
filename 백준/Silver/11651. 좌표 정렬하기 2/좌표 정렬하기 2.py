N = int(input())
dot_list = sorted([list(map(int, input().split())) for _ in range(N)])
dot_list = sorted(dot_list, key=lambda x: x[1])
for dot in dot_list:
    print(*dot)