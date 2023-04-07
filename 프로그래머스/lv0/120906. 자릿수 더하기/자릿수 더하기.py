def solution(n):
    # n 정수
    # n의 각 자릿수의 합을 return
    answer = 0
    n = str(n)
    
    for i in n:
        answer += int(i)
    
    return answer