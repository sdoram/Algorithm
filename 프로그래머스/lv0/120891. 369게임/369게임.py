def solution(order):
    # 3,6,9를 가진 리스트 만들기
    # 반복문과 조건문을 통해서 리스트와 일치 여부 확인
    answer = 0
    num_list = [3,6,9]
    order = str(order)
    for i in order:
        if int(i) in num_list:
            answer += 1
    return answer