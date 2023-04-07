def solution(n):
    answer = 0
    while n / 7 > answer:
        answer += 1
    return answer