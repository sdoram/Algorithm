def number(num):
    for n in range(1, len(num)):
        first_num = num[:n]
        last_num = num[n:]
        f_num = int(first_num[0])
        l_num = int(last_num[0])
        for i in range(1, len(first_num)):
            f_num *= int(first_num[i])
        for j in range(1, len(last_num)):
            l_num *= int(last_num[j])
        if f_num == l_num:
            return 'YES'
    return 'NO'


print(number(input()))