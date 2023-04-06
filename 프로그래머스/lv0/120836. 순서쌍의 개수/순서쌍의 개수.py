def solution(n):
    # n이 가질 수 있는 순서쌍 구하기
    # n을 돌릴 for문과 순서쌍인지 파악할 if문
    # 2중 for문?
    # 시간 초과 발생 <- n % one == 0인걸 찾으면 될듯?
    answer = 0
    
    for one in range(1, n+1):
        if n % one == 0:
            answer += 1
    
    return answer