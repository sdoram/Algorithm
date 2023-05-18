from sys import stdin

num_list = [int(stdin.readline()) for _ in range(9)]
print(max(num_list))
print(num_list.index(max(num_list)) + 1)