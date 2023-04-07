def solution(array):
    # 조건문으로 가장 큰 수 찾기
    # enumerate로 index 주기 
    answer = []
    max_num = 0
    index = 0
    
    for idx, arr in enumerate(array):
        if arr > max_num:
            max_num = arr
            index = idx
    answer = [max_num, index]
    return answer