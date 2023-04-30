def solution(a, d, included):
    # a = 등차수열 시작점, d = 공차
    # included = boolean 배열 
    # return은 true 항의 값만을 더한 결과
    answer = 0
    arithmetic_sequence = a
    for inc in included:
        if inc == True:
            answer += arithmetic_sequence
        arithmetic_sequence += d
    return answer