student_list = [0, 0, 0, 0]
for _ in range(int(input())):
    G, C, N = map(int, input().split())
    if G == 1:
        student_list[3] += 1
    elif C == 1 or C == 2:
        student_list[0] += 1
    elif C == 3:
        student_list[1] += 1
    elif C == 4:
        student_list[2] += 1

for i in student_list:
    print(i)
