def solution(arr):
    # n*n크기의 이차원 배열 arr
    # return은 arr[i][j] = arr[j][i] 이면 1 아니면 0 return
    # for문, 조건문을 통해서 i와 j 비교
    # print(len(arr))
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1