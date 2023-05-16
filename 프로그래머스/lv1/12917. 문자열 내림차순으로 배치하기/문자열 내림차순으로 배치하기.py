def solution(s):
    upper_list = []
    lower_list = []
    for word in s:
        if word.isupper():
            upper_list.append(word)
        else:
            lower_list.append(word)
    lower_list.sort(reverse=True)
    upper_list.sort(reverse=True)
    lower_list.extend(upper_list)
    return ''.join(lower_list)