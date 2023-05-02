def solution(sides):
    s = sorted(sides)
    answer = len(range(s[1],s[1]+s[0]))
    count = s[1]+1
    while s[1]+s[0] > count:
        answer += 1
        count += 1
    return answer