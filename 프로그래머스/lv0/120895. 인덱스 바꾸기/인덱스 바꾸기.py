def solution(my_string, num1, num2):
    # my_string = str, num1 & num2 = int
    # my_string[num1] , my_string[num2]
    answer = ''
    my_string_list = list(my_string)
    # num1과 num2에 해당하는 str
    str_1 = my_string_list[num1]
    str_2 = my_string_list[num2] 
    # 문자열 변경 
    my_string_list[num1] = str_2
    my_string_list[num2] = str_1
    
    answer = ''.join(my_string_list)
    return answer