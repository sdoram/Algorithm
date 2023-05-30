def solution(arr, queries):
    for s,e in queries:
        for i,a in enumerate(arr):
            if e >= i >= s:
                arr[i] += 1
    return arr