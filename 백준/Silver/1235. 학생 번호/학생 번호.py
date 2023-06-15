from sys import stdin


students = [stdin.readline().strip()[::-1] for _ in range(int(stdin.readline()))]


def students_number(students):
    while True:
        for i in range(len(students[0])):
            number = set([s[i::-1] for s in students])
            if len(students) == len(number):
                return len(list(number)[0])


print(students_number(students))