def solution(num_list, n):
    # num_list를 n개씩 묶어서 answer로 return
    # while문으로 num_list만큼 돌리고
    # reverse() 쓰고
    # for문으로 n만큼 pop()
    # n만큼 진행되면 answer에 append()
    answer = []
    num_list.reverse()

    while num_list:
        sum_num = []
        # n만큼 반복문 사용
        for _ in range(n):
            # 임시로 pop()한 list 모음
            sum_num.append(num_list.pop())
        # for문 탈출시 answer에 추가
        answer.append(sum_num)
    return answer