def solution(score):
    num_dict = {}
    for i, s in enumerate(score,1):
        num_dict[i] = sum(s)/2
    num_dict = sorted(num_dict.items(), reverse=True, key=lambda item: item[1])
    score_dict = [num[1] for num in num_dict]
    last_list = sorted([[num[0],score_dict.index(num[1])+1] for idx,num in enumerate(num_dict)])
    return [num[1] for num in last_list]