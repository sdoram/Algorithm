N = int(input())
level_dict = {i:int(input()) for i in range(N)}
count = 0
for i in range(N-1)[::-1]:
    if level_dict[i+1] <= level_dict[i]:
        count += level_dict[i] - level_dict[i+1] + 1
        level_dict[i] = level_dict[i+1] -1
print(count)