import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

students_list = [a-B for a in A]
answer = len(students_list)

for students in students_list:
    if students > 0:
        answer += (students-1) // C+1
print(answer)