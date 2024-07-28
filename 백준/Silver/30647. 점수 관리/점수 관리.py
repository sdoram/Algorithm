score_dict = {}
score_list = [input().split(':') for _ in range(int(input()))]
for i in score_list:
    score_dict[i[1].split(',')[0][1:-1]] = [i[2].split(',')[0], i[3][0]]
    
score_list = sorted([[key, list(map(int, value))] for key, value in score_dict.items()], key=lambda x: (-x[1][0], x[0]))
RANKING = [1, score_list[0][1][0]]
for i, s in enumerate(score_list, start=1):
    if RANKING[1] != s[1][0]:
        RANKING = [i, s[1][0]]
    if s[1][1] != 1:
        print(RANKING[0], s[0], s[1][0])