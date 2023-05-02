def solution(arr, queries):
    answer = []
    for q in queries:
        num = -1
        s,e,k = q[0], q[1], q[2]
        for a in arr[s:e+1]:
            if k < a:
                current_num = a
                if num > current_num or num == -1:
                    num = current_num
        answer.append(num)
    return answer