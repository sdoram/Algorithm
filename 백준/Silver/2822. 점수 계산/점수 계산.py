score_list = []
for num in range(1,9):
    score_list.append([int(input()),num])    
five_scores = sorted(score_list, reverse=True)[:5]
print(sum([score[0] for score in five_scores]))
print(*sorted([score[1] for score in five_scores]))
