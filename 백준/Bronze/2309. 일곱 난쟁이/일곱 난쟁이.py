num_list = sorted([int(input()) for _ in range(9)])
for num in num_list:
    find_num = sum(num_list) - 100 - num
    if find_num in num_list and num != find_num:
        num_list.pop(num_list.index(num))
        num_list.pop(num_list.index(find_num))
        break
[print(num) for num in num_list]