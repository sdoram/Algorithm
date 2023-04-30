import sys

scale_list = list(map(int, sys.stdin.readline().split()))
sorted_scale_list = sorted(scale_list)
reversed_scale_list = sorted(scale_list, reverse=True)

if scale_list == sorted_scale_list:
    print("ascending")
elif scale_list == reversed_scale_list:
    print("descending")
else:
    print("mixed")