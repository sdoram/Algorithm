def solution(dots):
    a = dots[0][0], dots[0][1]
    b = dots[1][0], dots[1][1]
    c = dots[2][0], dots[2][1]
    d = dots[3][0], dots[3][1]
    # (y2-y1)/(x2-x1) == (y4-y3)/(x4-x3)
    if (b[1]-a[1])/(b[0]-a[0]) == (d[1]-c[1])/(d[0]-c[0]):
        return 1
    if (c[1]-a[1])/(c[0]-a[0]) == (d[1]-b[1])/(d[0]-b[0]):
        return 1
    return 0
    