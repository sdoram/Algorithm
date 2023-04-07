def solution(numbers):
    # 곱하기를 위한 반복문
    # 최댓값 비교를 위한 조건문
    max_num = -100000000000000
    while numbers:
        pop_number = numbers.pop()
        for number in numbers:
            if pop_number * number > max_num:
                max_num = pop_number * number
        
    return max_num