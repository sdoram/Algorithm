def solution(s):
    list_s = s.split()
    answer = 0
    for i, num in enumerate(list_s,-1):
        if num == 'Z':
            answer -= int(list_s[i])
        else:
            answer += int(num)
    return answer