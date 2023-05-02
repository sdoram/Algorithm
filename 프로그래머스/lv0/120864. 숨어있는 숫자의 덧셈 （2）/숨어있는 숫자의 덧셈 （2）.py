def solution(my_string): 
    answer = 0
    num_list = []
    num = []
    for i,s in enumerate(my_string):
        if s.isdigit() and i+1 == len(my_string):
            num.append(i)
            num_list.append(num)
        elif s.isdigit():
            num.append(i)
        elif len(num) != 0:
            num_list.append(num)
            num = []
            
    for num in num_list:
        number = ''
        for n in num:
            number += my_string[n]
        answer += int(number)
    return answer