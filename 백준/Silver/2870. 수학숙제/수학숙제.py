import sys

input = sys.stdin.readline

homework = [input().rstrip() for _ in range(int(input()))]
number = []

for work in homework:
    num = ''
    for w in work:
        if w.isdigit():
            num += w
        elif num != '':
            number.append(int(num))
            num = ''
    if num != '':
        number.append(int(num))
    
for num in sorted(number):
    print(num)