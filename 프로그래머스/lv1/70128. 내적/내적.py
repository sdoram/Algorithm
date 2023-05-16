def solution(a, b):
    return sum([a[num]*b[num] for num in range(len(a))])