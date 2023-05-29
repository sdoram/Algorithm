def solution(arr):
    answer = []
    for a in arr:
        try:
            if answer[-1] != a:
                answer.append(a)
        except IndexError:
            answer.append(a)
    return answer