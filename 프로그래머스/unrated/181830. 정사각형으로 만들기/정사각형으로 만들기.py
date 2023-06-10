def solution(arr):
    for i,a in enumerate(arr):
        [arr[i].append(0) for _ in range(len(arr)-len(a))]
    for _ in range(len(a)-len(arr)):
        arr.append([0 for _ in range(len(arr[0]))])
    return arr