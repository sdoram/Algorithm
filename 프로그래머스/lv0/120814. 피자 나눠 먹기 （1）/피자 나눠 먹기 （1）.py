def solution(n):
    # n이 사람
    # 조건문으로 사람 수와 7조각을 비교
    # answer = 1 시작
    # 사람이 조각보다 많거나 같으면 answer += 1
    # 조각이 사람보다 많으면 answer 출력
    # 반복문 
    # anwer에 * 7조각수 / n >= 1:
    answer = 1
    
    while True:
        if 7 * answer / n >= 1:
            return answer
        else:
            answer += 1