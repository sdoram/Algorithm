def solution(arr):
    count = 0
    while True:
        arr_list = arr[::]
        for i,a in enumerate(arr):
            if a % 2 != 0 and a < 50:
                 arr[i] = a * 2 + 1
            elif a % 2 == 0 and a >= 50:
                arr[i] = a // 2
        if arr == arr_list:
            return count
        count += 1