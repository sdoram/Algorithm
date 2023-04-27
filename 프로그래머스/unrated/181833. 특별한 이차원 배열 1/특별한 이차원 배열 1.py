def solution(n):
    # n은 정수
    # return은 n*n의 이차원 배열
    # arr[i][j]의 값이 일치하는 부분의 원소는 1, 아니면 0
    # [[0]*n]*n으로 생성시 얕은 복사로 다른 원소 조작시 같은 인덱스의 원소 모두 변경 
    two_dimensional_array = [[0]*n for _ in range(n)]
    for j, i in enumerate(two_dimensional_array):
        i[j] = 1
    return two_dimensional_array