def solution(polynomial):
    p = polynomial.split()
    x_num = 0
    num = 0
    answer = ''
    for n in p:
        if 'x' in n and n[:-1].isdigit():
            x_num += int(n[:-1])
        elif 'x' in n:
            x_num += 1
        elif n.isdigit():
            num += int(n)
    if x_num == 1:
        answer = 'x'
    elif x_num != 0:
        answer = str(x_num)+'x'
    if num != 0 and x_num != 0:
        answer += f' + {str(num)}'
    elif num != 0:
        answer = str(num)
    return answer