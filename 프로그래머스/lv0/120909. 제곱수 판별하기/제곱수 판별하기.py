def solution(n):
    # 루트 n이 자연수인지 확인해라
    root_n = int(n**(1/2))
    if root_n == n**(1/2):
        return 1
    else:
        return 2