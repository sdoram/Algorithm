import sys
A, B = map(int, input().split())
A_num_list = list(map(int, sys.stdin.readline().split()))
B_num_list = list(map(int, sys.stdin.readline().split()))
A_num_list.extend(B_num_list)
print(*sorted(A_num_list))