def solution(array):
    # 중앙 값 구하기
    # len /2 시도하기
    # 숫자 정렬을 위한 sort()사용
    array.sort()
    median = len(array)//2
    answer = array[median]
    
    
    
    return answer