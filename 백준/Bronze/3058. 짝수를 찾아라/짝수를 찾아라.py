for _ in range(int(input())):
    num_list = list([num for num in map(int, input().split()) if num % 2 == 0])
    print(sum(num_list), min(num_list))
