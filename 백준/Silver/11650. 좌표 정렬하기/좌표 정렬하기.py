dot_list = []
for _ in range(int(input())):
    dot_list.append(list(map(int, input().split())))
dot_list.sort()
for dot in dot_list:
    print(*dot)