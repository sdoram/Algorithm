def election():
    candidate = [int(input()) for _ in range(int(input()))]
    candidate_dict = dict()
    for i, c in enumerate(candidate, start=1):
        if c not in candidate_dict:
            candidate_dict[c] = [i]
        else:
            candidate_dict[c] += [i]
    # 중복 최다 득표자 확인
    if len(candidate_dict[max(candidate_dict.keys())]) > 1:
        return 'no winner'
    else:
        # 과반 이상 득표
        if sum([key*len(value) for key, value in candidate_dict.items()]) - max(candidate_dict.keys()) < max(candidate_dict.keys()):
            return f'majority winner {candidate_dict[max(candidate_dict.keys())][0]}'
        # 과반 미만 득표
        else:
            return f'minority winner {candidate_dict[max(candidate_dict.keys())][0]}'

for _ in range(int(input())):
    print(election())
