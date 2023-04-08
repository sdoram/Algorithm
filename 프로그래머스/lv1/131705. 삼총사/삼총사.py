def solution(number):
    # 3명의 숫자를 더해서 0이 되면 삼총사
    # 2중 for문?
    # 1개를 pop으로 빼고 나머지 2자리를 for문으로 돌린다
    answer = 0
    while len(number) >= 3:
        pop_num1 = number.pop()
        # pop으로 빠진 상태의 number를 복사
        copy_number = number[::]
        while len(copy_number) >= 2:
            pop_num2 = copy_number.pop()
            for num in copy_number:
                if pop_num1 + pop_num2 + num == 0:
                    answer += 1
    return answer