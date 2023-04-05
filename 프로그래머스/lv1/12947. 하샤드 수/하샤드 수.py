def solution(x):
    # x가 18일 때 1+8 = 9로 18이 나눠지는 수 검사하기
    # 자릿수마다 추출하고 조건문으로 True, False확인하기
    str_x = str(x)
    y = 0
    
    for i in str_x:
        y += int(i)
        
    if x % y == 0:
        return True
    else:
        return False