bin_str = input()
zero_bin_str_list = bin_str.split('0')
one_bin_str_list1 = bin_str.split('1')
reverse_one = 0
reverse_zero = 0

for s in zero_bin_str_list:
    if s != '':
        reverse_one += 1

for s in one_bin_str_list1:
    if s != '':
        reverse_zero += 1
print(reverse_zero if reverse_zero <= reverse_one else reverse_one)
