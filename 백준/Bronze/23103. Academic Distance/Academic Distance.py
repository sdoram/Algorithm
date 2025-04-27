n = int(input())
a, b = map(int, input().split())
total_distance = 0
for i in range(n-1):
    x, y = map(int, input().split())
    total_distance += abs(x-a) + abs(y-b)
    a, b = x, y
print(total_distance)