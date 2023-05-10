score_list = [[int(input()),num] for num in range(1,9)]
five_scores = sorted(score_list, reverse=True)[:5]
print(sum([score[0] for score in five_scores]))
print(*sorted([score[1] for score in five_scores]))
