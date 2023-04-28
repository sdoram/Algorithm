def solution(str1, str2):
    # zip으로 묶고 언패킹?
    answer = ''
    list_zip = list(zip(str1, str2))
    for n in list_zip:
        for i in n:
            answer += i
    return answer