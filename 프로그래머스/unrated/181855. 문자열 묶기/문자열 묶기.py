def solution(strArr):
    arr_len = {}
    for a in strArr:
        if len(a) not in arr_len:
            arr_len[len(a)] = 1
        else:
            arr_len[len(a)] += 1
    return sorted(arr_len.values(),reverse=True)[0]