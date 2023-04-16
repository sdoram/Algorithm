def solution(array):
    # 정수를 가진 리스트에서 7의 갯수 세기
    answer = 0
    num_join = ''.join(map(str, array))
    answer = num_join.count('7')
    return answer