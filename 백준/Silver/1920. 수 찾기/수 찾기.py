from sys import stdin

N = stdin.readline()
find_set = set(list(map(int, stdin.readline().split())))
M = stdin.readline()
my_list = list(map(int, stdin.readline().split()))
for num in my_list:
    print(1 if num in find_set else 0)