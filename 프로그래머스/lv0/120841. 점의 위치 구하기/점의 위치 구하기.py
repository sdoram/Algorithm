def solution(dot):
    # dot[0] = x, dot[1] = y
    # x,y가 양수인지 음수인지 판별해서 속해있는 사분면 구하기
    # 양수x 양수y = 1
    # 음수x 양수y = 2
    # 음수x 음수y = 3
    # 양수x 음수y = 4
    # 조건문 사용하기 
    
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    elif dot[0] > 0 and dot[1] < 0:
        return 4