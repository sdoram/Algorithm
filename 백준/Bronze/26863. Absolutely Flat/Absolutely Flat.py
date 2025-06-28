leg_list = [int(input()) for _ in range(4)]
pad = int(input())

if min(leg_list) == max(leg_list):
    print(1)
elif min(leg_list) + pad == max(leg_list) and leg_list.count(min(leg_list)) == 1:
    print(1)
else:
    print(0)