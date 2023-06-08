def solution(arr):
    i = 0
    stk = []
    for _ in range(len(arr)):
        if stk == [] :
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            stk.pop()
            i += 1
        elif stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1
    return stk if stk else [-1]