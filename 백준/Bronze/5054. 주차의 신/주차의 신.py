for _ in range(int(input())):
    input()
    num_list = list(map(int, input().split()))
    print((max(num_list)-min(num_list)) * 2)