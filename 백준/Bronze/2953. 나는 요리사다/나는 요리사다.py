score_list = [sum(map(int, input().split())) for _ in range(5)]
print(score_list.index(max(score_list)) + 1, max(score_list))
