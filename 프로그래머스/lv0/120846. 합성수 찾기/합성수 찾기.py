def solution(n):
    # n이하의 약수가 3개 이상인 수 찾기
    # range로 반복문
    # 2중 for문으로 약수의 갯수 체크?
    divisor = 0
    answer = 0
    
    for i in range(1, n+1):
        divisor = 0
        for x in range(1, i+1):
            if i % x == 0:
                divisor += 1
        if divisor >= 3:
            answer += 1
    
    return answer