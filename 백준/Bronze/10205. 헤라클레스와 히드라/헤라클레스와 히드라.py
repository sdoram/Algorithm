for i in range(1, int(input())+1):
    head = int(input())
    action = sum([1 if a == 'c' else -1 for a in input()])
    print(f'Data Set {i}:')
    print(head + action)
    print()