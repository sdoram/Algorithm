def solution(num_list):
    answer = []
    for i in range(1, len(num_list)+1):
        a = num_list.pop()
        answer.append(a)
    return answer