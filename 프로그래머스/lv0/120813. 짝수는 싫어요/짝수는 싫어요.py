def solution(n):
    # n은 정수
    # 홀수를 오름차순으로 return
    answer = []
    
    for i in range(1, n+1, 2):
        answer.append(i)
        
    
    return answer