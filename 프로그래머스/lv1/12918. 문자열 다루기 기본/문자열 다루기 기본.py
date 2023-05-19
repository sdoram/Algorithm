def solution(s):
    if sum([1 for i in s if i.isdigit()]) == len(s):
        if len(s) == 4 or len(s) == 6:
            return True
    return False