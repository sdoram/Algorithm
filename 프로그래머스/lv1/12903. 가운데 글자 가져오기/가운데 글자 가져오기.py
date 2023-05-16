def solution(s):
    median = (len(s)-1) // 2+1
    return s[median-1: median+1] if len(s) % 2 == 0 else s[median-1] 