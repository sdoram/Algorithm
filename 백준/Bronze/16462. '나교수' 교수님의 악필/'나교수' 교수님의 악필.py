score_list = [input() for _ in range(int(input()))]
new_score_list = []
for score in score_list:
    new_score = ''
    for s in score:
        if s == '0' or s == '6':
            new_score += '9'
        else:
            new_score += s
    new_score_list.append(min(int(new_score), 100))
average_score = sum(new_score_list) / len(score_list)
print(int(average_score)+1 if average_score - int(average_score) >= 0.5 else int(average_score))