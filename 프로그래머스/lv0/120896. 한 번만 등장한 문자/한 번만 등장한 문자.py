def solution(s):
    s_dict = {}
    for i in s:
        if i not in s_dict:
            s_dict[i] = 1
        elif i in s_dict:
            s_dict[i] += 1
    return ''.join([i for i in sorted(s_dict.keys()) if s_dict[i] == 1])