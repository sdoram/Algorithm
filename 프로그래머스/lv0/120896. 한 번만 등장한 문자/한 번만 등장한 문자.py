def solution(s):
    # 문자열 s
    # in으로 확인하기 
    answer = ''
    s_list = {}
    for i in s:
        if i in s_list:
            s_list[i] += 1
        elif not i in s_list:
            s_list[i] = 1
    for i in sorted(s_list.keys()):
        if s_list[i] == 1:
            answer += i
    return answer