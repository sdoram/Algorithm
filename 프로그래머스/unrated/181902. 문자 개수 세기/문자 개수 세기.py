import string
def solution(my_string):
    num_list = [0 for _ in range(52)]
    for a in my_string:
        if a.isupper():
            num_list[string.ascii_uppercase.index(a)] += 1
        else:
            num_list[string.ascii_lowercase.index(a)+26] += 1
    return num_list