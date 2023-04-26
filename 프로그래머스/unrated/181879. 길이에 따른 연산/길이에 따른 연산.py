def solution(num_list):
    return sum(num_list) if len(num_list) > 10 else eval('*'.join([str(num) for num in num_list]))