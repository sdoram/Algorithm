N = int(input())
num_list = list(map(int, input().split()))
print(len(num_list) - len(set(num_list)))
