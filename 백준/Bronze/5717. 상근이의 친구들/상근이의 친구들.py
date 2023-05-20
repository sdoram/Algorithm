while True:
    FRIENDS = list(map(int, input().split()))
    if sum(FRIENDS) == 0:
        break
    print(sum(FRIENDS))