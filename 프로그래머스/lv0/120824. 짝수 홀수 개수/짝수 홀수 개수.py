def solution(num_list):
    # num_list는 정수가 담긴 리스트
    # answer = 짝수와 홀수의 갯수
    # for문
    answer = []
    odd_number = 0
    even_number = 0
    
    for num in num_list:
        if num % 2 ==0:
            even_number +=1
        else:
            odd_number +=1
            
    answer.append(even_number)
    answer.append(odd_number)
    return answer