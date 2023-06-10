def solution(strArr):
    arr_len = {}
    for a in strArr:
            arr_len[len(a)] = arr_len.get(len(a), 0) + 1
    return sorted(arr_len.values(),reverse=True)[0]
