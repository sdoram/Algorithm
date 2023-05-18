bin_num = input().split()
sum_num = int(bin_num[0], 2) + int(bin_num[1], 2)
print(bin(sum_num)[2:])