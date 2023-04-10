count = 0
max_num = 0
while count < 9:
    count += 1
    a = int(input())
    if max_num < a:
        max_num = a
        num_count = count

print(max_num)
print(num_count)
