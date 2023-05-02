import sys
num_list = []
for _ in range(9):
    num_list.append(list(map(int, sys.stdin.readline().split())))

max_num = num_list[0][0]
max_num_location = [1, 1]
for i1, num1 in enumerate(num_list, 1):
    for i2, num2 in enumerate(num1, 1):
        if max_num < num2:
            max_num = num2
            max_num_location = [i1, i2]
print(max_num)
print(*max_num_location)