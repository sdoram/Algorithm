def solution(arr, k):
    answer = []
    for a in arr:
        if a not in answer:
            answer.append(a)
        if len(answer) == k:
            return answer
    return answer + [-1 for _ in range(k - len(answer))]