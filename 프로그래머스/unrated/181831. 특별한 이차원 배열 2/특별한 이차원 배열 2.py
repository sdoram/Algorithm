def solution(arr):
    # n*n의 배열 arr
    # return은 i[j] 와 [j]i의 값이 동일하면 1 아니면 0
    # 기본값을 1로주고 for문으로 확인하다가 0이면 return
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0    
    return 1