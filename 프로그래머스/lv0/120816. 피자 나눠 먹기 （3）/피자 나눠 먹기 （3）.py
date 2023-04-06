def solution(slice, n):
    answer = 1
    # 피자 조각수 2~12
    # n명의 사람이 한조각 이상 먹기
    # 몫이 0이면 while문 반복
    # 인당 1조각이 넘으면 멈춤
    while slice*answer // n == 0:
        answer += 1
    return answer