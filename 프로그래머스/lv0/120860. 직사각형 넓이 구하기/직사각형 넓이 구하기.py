def solution(dots):

    # x,y 좌표가 담겨있는 배열을 dots로 직사각형 넓이 함수를 리턴

    # dots = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]

    # 주어진 좌표는 직사각형의 변이 축과 평행하기 때문에, 좌표들 중 가장 작은 x좌표와 가장 큰 x좌표를 각각x_min,x_max로
    # 가장 작은 y좌표와 가장 큰 y_좌표를 각각 y_min, y_max로 찾아서 두 좌표 사이의 거리를 곱하면 직사각형의 넓이

    # min함수와 max 함수는 'dots' 리스트에 있는 각 꼭지점 좌표를 순회하며, 람다 함수를 이용하여 x좌표와 y좌표를 비교하고 가장
    # 작은 x좌표와 가장 큰x좌표, 가장 작은 y좌표와 가장 큰 y_좌표를 각각 x_min, x_max, y_min, y_max 변수의 저장
    x_min = min(dots, key=lambda x: x[0])[0]
    x_max = max(dots, key=lambda x: x[0])[0]
    y_min = min(dots, key=lambda x: x[1])[1]
    y_max = max(dots, key=lambda x: x[1])[1]


    return (x_max - x_min) * (y_max - y_min)