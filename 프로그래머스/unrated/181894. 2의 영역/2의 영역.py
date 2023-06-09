def solution(arr):
    two_list = [i for i in range(len(arr)) if arr[i] == 2]
    try:
        return arr[two_list[0]:two_list[-1]+1]
    except IndexError:
        return [-1]