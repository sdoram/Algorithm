def solution(array, n):
    array.sort()
    find_num = abs(array[0] - n)
    answer = array[0]
    for arr in array:
        current_num = abs(arr - n)
        if find_num > current_num:
            find_num = current_num
            answer = arr
    return answer