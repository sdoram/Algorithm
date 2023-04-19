alpha_list = [0]*26
str_input = input()

for str_ in str_input:
    alpha_num = ord(str_) - ord('a')
    alpha_list[alpha_num] += 1
    # List Comprehension
str_alpha_list = [str(x)for x in alpha_list]
print(' '.join(str_alpha_list))