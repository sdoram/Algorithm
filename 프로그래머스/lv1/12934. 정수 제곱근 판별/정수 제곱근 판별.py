def solution(n):
    # n은 양의 정수, x의 제곱인지 아닌지 판단
    # for문으로 n을 돌림
    # 효율성 최적화 하고 싶은데 모르겠다.
    
    answer = -1
    
    for x in range(1, n+1):
        if x * x == n:
            answer = (x+1)*(x+1)
            break
        
    return answer