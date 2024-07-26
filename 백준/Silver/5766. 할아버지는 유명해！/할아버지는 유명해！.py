while True:
    N, M = map(int, input().split())
    if N+M == 0:
        break
    
    score_dict = {}

    for _ in range(N):
        players = list(map(int, input().split()))
        
        for p in players:
            if p not in score_dict:
                score_dict[p] = 1
            else:
                score_dict[p] += 1
    second = sorted([s for s in score_dict.values()], reverse=True)[1]
    print(*sorted([key for key, value in score_dict.items() if value == second]))