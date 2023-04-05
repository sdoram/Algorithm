def solution(seoul):
    # 매개변수는 list안에 str이 담겨있음
    # list안에서 'Kim'의 위치 찾기
    # find함수?
    # for문
    answer = ''
    num = 0
    
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            num = i
    answer = f'김서방은 {num}에 있다'
    return answer