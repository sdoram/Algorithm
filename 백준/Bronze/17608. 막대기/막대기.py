from sys import stdin

stick_list = []
for _ in range(int(stdin.readline())):
    stick_list.append(int(stdin.readline()))

height = 0
count = 0
for i in stick_list[::-1]:
    if i > height:
        height = i
        count += 1
print(count)
