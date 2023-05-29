def solution(arr, intervals):
    new_list = [arr[j:k+1] for j,k in intervals]
    answer = []
    for a in new_list:
        answer.extend(a)
    return answer