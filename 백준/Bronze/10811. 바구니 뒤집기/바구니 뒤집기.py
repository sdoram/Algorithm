n, m = map(int, input().split())
num_list = []
count = 0
revers_count = 0

while count < n:
    count += 1
    num_list.append(count)

while revers_count < m:
    revers_count += 1
    start_num, end_num = map(int, input().split())
    start_num -= 1
    revers_list = []
    reversed(num_list[start_num:end_num])
    revers_list = num_list[start_num:end_num]

    for index in range(start_num, end_num):
        num_list[index] = revers_list.pop()

answer = ' '.join(map(str, num_list))
print(answer)
