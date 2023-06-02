def solution(str_list):
    for i,s in enumerate(str_list):
        if s in 'l':
            return str_list[:i]
        if s in 'r':
            return str_list[i+1:]
    return []