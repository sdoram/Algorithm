import string
def solution(s, n):
    answer = ''
    upper_alpha = string.ascii_uppercase
    lower_alpha = string.ascii_lowercase
    for w in s:
        if w in upper_alpha:
            w = upper_alpha[upper_alpha.index(w)+n-26]
        elif w in lower_alpha:
            w = lower_alpha[lower_alpha.index(w)+n-26]
        answer += w
    return answer