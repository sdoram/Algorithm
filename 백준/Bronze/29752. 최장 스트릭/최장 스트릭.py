input()
S = map(int, input().split())
count_list = []
count = 0
for s in S:
    if s:
        count += 1
    else:
        count_list.append(count)
        count = 0
count_list.append(count)
print(max(count_list))