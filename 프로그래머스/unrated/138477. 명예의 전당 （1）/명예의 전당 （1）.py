def solution(k, score):
    answer = []
    k_list = []
    for i in range(len(score)):
        k_list.append(score[i])
        if len(k_list) > k:
            k_list.pop(k_list.index(min(k_list)))
        answer.append(min(k_list))
    return answer