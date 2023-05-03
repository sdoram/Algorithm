def solution(arr):
    stk = []
    i = 0
    while i != len(arr):
        if stk == []:
            stk.append(arr[i])
            i += 1
        if stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            stk.pop()
    return stk