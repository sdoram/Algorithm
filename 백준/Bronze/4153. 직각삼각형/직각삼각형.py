while True:
    num_list = list(map(int, input().split()))
    if num_list == [0, 0, 0]:
        break
    num_list = [i ** 2 for i in num_list]
    max_num = num_list.pop(num_list.index(max(num_list)))
    num1 = num_list[0]
    num2 = num_list[1]
    if max_num - (num1+num2) == 0:
        print('right')
    else:
        print('wrong')