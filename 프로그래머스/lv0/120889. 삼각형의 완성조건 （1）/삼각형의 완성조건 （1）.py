def solution(sides):
    # 정수가 3개 있는 리스트에서 가장 큰 값이 다른 두개의 값을 더한 것 보다 작으면 1, 크면 2
    # sort로 정렬하고 나머지 두개의 값을 더한 조건문으로 해결
    sides.sort()
    max_side = sides.pop()

    if max_side < sides[0] + sides[1]:
        return 1
    else:
        return 2
