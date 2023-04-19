def solution(dots):
    # dots = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    x = [dots[x][0] for x in range(len(dots))]
    y = [dots[y][1] for y in range(len(dots))]
    answer = (max(x) - min(x)) * (max(y) - min(y))
    return answer