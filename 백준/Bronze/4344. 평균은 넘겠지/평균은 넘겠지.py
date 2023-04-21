a = int(input())
for _ in range(a):
    scores = list(map(int, (input().split())))
    students = scores.pop(0)
    total_score = sum(scores)
    average_score = total_score // students
    over_score_raito = format(
        len([i for i in scores if i > average_score]) / len(scores) * 100, ".3f")
    print(f'{over_score_raito}%')