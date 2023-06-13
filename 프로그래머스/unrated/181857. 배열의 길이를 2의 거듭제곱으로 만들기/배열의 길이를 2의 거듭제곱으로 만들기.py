def solution(arr):
    count = 0
    while True:
        lens = pow(2,count)
        if len(arr) <= lens:
            break
        count += 1
    [arr.append(0) for _ in range(lens-len(arr))]
    return arr