def solution(phone_number):
    # 뒤의 4자리를 제외한 나머지를 *로 변환
    # [:-4]?
    answer = ''
    
    for _ in phone_number[:-4]:
        answer += '*'
    answer += phone_number[-4:]
    
    return answer