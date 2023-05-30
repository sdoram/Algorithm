def solution(date1, date2):
    answer = 0
    for d1, d2 in zip(date1, date2):
        if d1 < d2:
            return 1
        elif d2 < d1:
            return 0
    return answer