# 입력된 수를 짝수,  % 2
# 입력된 수가 홀수, *3 +1
# 이 작업을 1이 될때까지 반복
# 반복 횟수 500 이하인 경우 반복 횟수 출력
# 주어진 값이 1인 경우 0 출력
# 반복 횟수 500 이상인 경우 -1 출력

def solution(num):
    answer = 0

    if num == 1:
        return 0

    while num > 1:
        answer += 1
        # 짝수일 때
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1

        if answer == 500:
            return -1
    return answer