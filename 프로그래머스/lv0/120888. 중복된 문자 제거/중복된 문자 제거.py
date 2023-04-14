def solution(my_string):
    answer = ''
    my_dict = {}
    # 딕셔너리 key값으로 존재하는지 확인하고 중복 체크
    for str_ in my_string:
        if str_ not in my_dict:
            my_dict[str_] = 1
            answer += str_

    return answer