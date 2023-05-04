def solution(n):
    # 3이거나 3의 배수이면 +1
    answer = 0
    count = 0
    while count != n:
        answer += 1
        if answer % 3 ==0 or '3' in str(answer):
            continue
        count += 1
    return answer