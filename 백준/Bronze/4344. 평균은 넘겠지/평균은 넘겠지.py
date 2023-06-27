a = int(input())
for _ in range(a):
    scores = list(map(int, (input().split())))
    students = scores.pop(0)
    total_score = sum(scores)
    average_score = total_score // students
    over_score_raito = list(str(format(
        len([i for i in scores if i > average_score]) / len(scores) * 100, ".4f")))
    if int(over_score_raito[-1]) >= 5:
    	over_score_raito[-2] = str(int(over_score_raito[-2]) + 1)
    print(f"{''.join(over_score_raito[:-1])}%")