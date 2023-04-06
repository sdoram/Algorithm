def solution(my_string, n):
    # 매개변수 str, int
    # my_string의 각 문자를 n만큼 반복
    # for문 사용
    answer = ''
    
    for my_str in my_string:
        answer += my_str*n
        
    return answer