from sys import stdin

for _ in range(int(stdin.readline())):
    school_list = []
    for _ in range(int(stdin.readline())):
        school_list.append(stdin.readline().split())
    sorted_list = sorted(school_list, key=lambda x: int(x[1]))
    print(sorted_list[-1][0])