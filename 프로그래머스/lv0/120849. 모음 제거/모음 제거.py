def solution(my_string):
    # a,e,i,o,u 를 제거한 my_string을 반환해라
    # list로 모음을 만든다
    # for문으로 my_string에 모음이 있는지 확인한다. 
    answer = ''
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    
    for my_str in my_string:
        if not my_str in vowel_list:
            answer += my_str
    
    return answer