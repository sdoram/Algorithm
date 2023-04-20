def solution(dots):
    # dots = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    # return 은 직사각형의 넓이
    # 1,1 -1,-1 == 1 -1 차이만 구하면 됩니다.
    # 가장 큰 값 - 가장 작은 값 == 길이 1 - -1 == 2
    # for , sort, 
    # max, min 
    return (max(dots)[0] -min(dots)[0]) * (max(dots)[1] - min(dots)[1])