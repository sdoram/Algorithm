def solution(s1, s2):
    # s1,s2 str을 가진 list
    # return s1,s2이 가진 동일한 원소의 갯수
    # 비교를 위한 조건문, 반복문
    answer = 0
    for n1 in s1:
        for n2 in s2:
            if n1 == n2:
                answer += 1
    return answer