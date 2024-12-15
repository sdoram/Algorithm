point_list = [list(map(int, input().split())) for _ in range(int(input()))]
A = max([point[0] for point in point_list])
B = min([point[0] for point in point_list])
C = max([point[1] for point in point_list])
D = min([point[1] for point in point_list])
print((A-B)*2 + (C-D)*2)