from sys import stdin

COUNT = 0
while True:
    COUNT += 1
    N = int(stdin.readline())
    if N == 0:
        break
    students = [stdin.readline().strip() for _ in range(N)]
    check_list = []
    for _ in range(N * 2 - 1):
        check = int(stdin.readline().split()[0])
        if check in check_list:
            check_list.remove(check)
        else:
            check_list.append(check)
    print(COUNT, students[check_list[0] - 1])