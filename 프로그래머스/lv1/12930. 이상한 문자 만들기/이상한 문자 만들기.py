def solution(s):
    answer = ''
    count = 0
    for w in s:
        answer += w.lower() if count % 2 else w.upper()
        count += 1
        if w == ' ':
            count = 0
    return answer