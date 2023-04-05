def solution(a, b):
    # a와 b 사이에 속한 정수의 합 구하기
    # for문으로 range(a, b) 사용해보기
    # a == b일 경우 a or b 출력
    # a와 b중에 큰 수를 넣어야함 <- 변수 선언해서 넣기
    answer = 0
    min_num = 0
    max_num = 0
    
    if a > b:
        max_num = a
        min_num = b
    elif b > a:
        max_num = b
        min_num = a
    elif a == b:
        max_num = a
        min_num = a
    
    for num in range(min_num,max_num+1):
        answer += num
    
    return answer