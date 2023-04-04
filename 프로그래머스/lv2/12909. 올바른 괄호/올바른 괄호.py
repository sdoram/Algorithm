def solution(s):
    answer = 0
    # '('가 생기면 +1 ,')'가 생기면 -1
    # ')'가 먼저 나와서 -1이 되면 바로 False 리턴 
    
    for i in s:
        if answer == -1:
            return False
        if i == '(':
            answer += 1
        else:
            answer -= 1
            
    if answer == 0:
        return True
    else:
        return False