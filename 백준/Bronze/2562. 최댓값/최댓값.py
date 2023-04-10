max_num = 0
for index in range(1, 10):
    a = int(input())
    if max_num < a:
        max_num = a
        num_count = index
print(max_num)
print(num_count)
