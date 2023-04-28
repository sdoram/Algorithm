find_start, find_end = map(int, input().split())
start, end = 1, 45
num_list = []

while start <= end:
    for num in range(start):
        num_list.append(start)
    start += 1
print(sum(num_list[find_start-1:find_end]))