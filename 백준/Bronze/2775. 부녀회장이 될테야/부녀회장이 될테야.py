for _ in range(int(input())):
    num_list1 = []
    num_list2 = []
    persons = 0
    k = int(input())
    n = int(input())
    for num in range(1, n+1):
        persons += num
        num_list1.append(persons)
    for _ in range(k-1):
        for idx, num in enumerate(num_list1[::], 1):
            num_list2.append(sum(num_list1[:idx]))
        num_list1 = num_list2
        num_list2 = []
    print(num_list1[-1])