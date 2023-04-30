def solution(code):
    # 1일 때 홀수만 추가 
    # 0일 때 짝수만 추가 
    mode = 0
    answer = ''
    for i,n in enumerate(code):
        if n == '1' and mode == 1:
            mode = 0
            continue
        elif n == '1':
            mode = 1
            continue
        if mode == 1 and i % 2 != 0:
            answer += n
        elif mode == 0 and i % 2 == 0:
            answer += n
    return answer if len(answer) != 0 else 'EMPTY'