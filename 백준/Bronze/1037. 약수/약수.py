num = int(input())
divisor_list = sorted(list(map(int, input().split())))
print(divisor_list[0]*divisor_list[-1])