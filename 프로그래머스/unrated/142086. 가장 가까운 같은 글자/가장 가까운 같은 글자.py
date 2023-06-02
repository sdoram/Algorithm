def solution(s):
    answer = []
    s_dict = {}
    for i, w in enumerate(s):
        if w not in s_dict:
            answer.append(-1)
            s_dict[w] = i
        else:
            answer.append(i - s_dict[w] )
            s_dict[w] = i
    return answer