def solution(n):
    # n은 정수
    # return은 n*n의 이차원 배열
    # arr[i][j]의 값이 일치하는 부분의 원소는 1, 아니면 0
    two_dimensional_array = [[0]*n for i in range(n)]
    for i, j in enumerate(two_dimensional_array):
        j[i] = 1
    return two_dimensional_array