num = sorted(list(map(int, input().split())))
print(1 if num[0] + num[1] == num[2] else 2 if num[0] * num[1] == num[2] else 3)