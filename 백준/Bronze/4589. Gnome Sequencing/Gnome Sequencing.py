print('Gnomes:')
for _ in range(int(input())):
    NUM_LIST = list(map(int, input().split()))
    if sorted(NUM_LIST) == NUM_LIST or sorted(NUM_LIST, reverse=True) == NUM_LIST:
        print('Ordered')
    else:
        print('Unordered')