def solution(num, total):
    # while문으로 +1씩 계속 증가
    # for문으로 num만큼 반복
    # count의 정확한 초기값을 어떻게 주지?
    count = -100
    while True:
        answer = []
        sum_num = 0
        
        for i in range(count, count+num):
            sum_num += i
            answer.append(i)
        if total == sum_num:
            return answer
        count += 1