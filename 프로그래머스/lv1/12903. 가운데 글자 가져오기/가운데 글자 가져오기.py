def solution(s):
    median = (len(s)-1) // 2
    return s[median:median+2] if len(s) % 2 == 0 else s[median] 