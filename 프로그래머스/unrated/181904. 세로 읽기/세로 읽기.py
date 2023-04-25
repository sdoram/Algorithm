def solution(my_string, m, c):
    # my_string = 문자열  m,c = 정수
    # return은 m,c를 이용한 my_string
    # 슬라이싱 사용
    answer = ''
    for i in my_string[c-1::m]:
        answer += i
    return answer