a = int(input())
c = input().split()
max_num = int(c[0])
min_num = int(c[0])
for i in c[:a]:
    if int(i) > max_num:
        max_num = int(i)
    if int(i) < min_num:
        min_num = int(i)

print(min_num, max_num)