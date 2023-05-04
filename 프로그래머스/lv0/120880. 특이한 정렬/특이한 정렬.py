def solution(numlist, n):
    numdict = {}
    for num in sorted(numlist, reverse=True):
        numdict[num] = abs(num - n)
    numdict = sorted(numdict.items(), key=lambda x:x[1])
    return [x[0] for x in numdict]