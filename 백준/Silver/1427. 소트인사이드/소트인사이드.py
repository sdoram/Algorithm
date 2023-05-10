num = input()
num_list = []
for n in num:
    num_list.append(n)
print(''.join(sorted(num_list, reverse=True)))