def solution(my_string):
    # my_sting을 list로 변환한 집합을 받을 변수 선언
    
    answer = ''
    # set은 중복 값을 제거함
    check = list(set(my_string))
    for str_ in my_string:
        # pop으로 빠지면 if문 진입 X 
        if str_ in check:
            # index()로 str_의 위치 찾기
            # pop(index())로 위치 지정해서 pop하기
            answer += check.pop(check.index(str_))
            # print(check)
            # print(answer)
            
    
    return answer