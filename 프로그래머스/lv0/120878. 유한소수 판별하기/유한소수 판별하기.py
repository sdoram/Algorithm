def solution(a, b):
    if a % b == 0:
        return 1
    count = 2
    while count <= b:
        if a % count == 0 and b % count == 0:
            a //= count
            b //= count
            continue
        count += 1
    # 분모가 2와 5로만 이루어졌는지 확인할 방법 
    while b != 1:
        if b % 2 == 0:
            b //= 2
            continue
        if b % 5 == 0:
            b //= 5
            continue
        return 2
    return 1
        