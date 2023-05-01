def solution(my_string):
    answer_list = [s for s in my_string.lower()]
    answer_list.sort()
    return ''.join(answer_list)