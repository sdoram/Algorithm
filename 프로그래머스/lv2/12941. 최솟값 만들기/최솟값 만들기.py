def solution(A,B):
    answer = 0
    # 정렬, 최솟값 구할 준비 
    A.sort()
    B.sort(reverse=True)
    
    for i in range(1,(len(A)+1)):
        A_num = A.pop()
        B_num = B.pop()
        # A와B 에서 각각 하나씩 뽑아서 곱하는걸 누적
        answer += A_num * B_num
    return answer
