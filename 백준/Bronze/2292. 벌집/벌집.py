count = 1
num = int(input())
search_num = 1
if num == 1:
    print(count)
else:
    while True:
        search_num += 6 * count
        count += 1
        if search_num >= num:
            print(count)
            break