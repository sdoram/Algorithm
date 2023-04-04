def solution(n):
    # n = 자연수
    # n % x == 1을하는 가장 작은 자연수x 구하기
    # while문? 
    x = 0
    
    while True:
        x += 1
        if n % x == 1:
            break
    
    return x
