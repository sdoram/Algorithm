def solution(a, b, c, d):
    # 주사위가 모두 같다면 1111*p
    # 세개가 p로 같다면 (10*p +q)**2
    # 두개 씩 같다면 (p+q) * |p - q|
    # 두개만 p로 같다면 q*r
    # 다 다르면 가장 작은 정수
    
    
    num_list = sorted([a,b,c,d])
    if num_list.count(num_list[0]) == 4:
        return 1111*num_list[0]
    elif num_list.count(num_list[0]) == 3:
        return pow(10*num_list[0] +num_list[3], 2)
    elif num_list.count(num_list[3]) == 3:
        return pow(10*num_list[1] +num_list[0], 2)
    elif num_list.count(num_list[0]) == 2 and num_list.count(num_list[2]) == 2:
        return (num_list[0]+num_list[2]) * abs(num_list[0] - num_list[2])
    elif len(set(num_list)) == 4:
        return num_list[0]
    answer = []
    for num in num_list:
        if num_list.count(num) == 1:
            answer.append(num)
    return answer[0] * answer[1]
    