for _ in range(int(input())):
    player_list = []
    for _ in range(int(input())):
        player_list.append(list(input().split()))
    print(sorted(player_list, key=lambda x: int(x[0]))[-1][1])
