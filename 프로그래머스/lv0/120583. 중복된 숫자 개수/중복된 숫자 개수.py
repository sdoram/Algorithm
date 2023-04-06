def solution(array, n):
    # array에 있는 n의 갯수 구하기
    # for문
    # n과 같은지 체크하는 if문
    answer = 0
    
    for arr in array:
        if arr == n:
            answer +=1
    
    return answer