def solution(rank, attendance):
    # rank는 등수, attendance는 참석 여부
    # 1등부터 차례대로 참석가능한 3명 구하기
    a_list = []
    # 오름차순으로 1등부터 확인
    for r in sorted(rank):
        print(r, rank.index(r))
        # attendance의 [r의index와 동일한 index]가 True라면
        if attendance[rank.index(r)]:
            # index 번호를 추가 
            a_list.append(rank.index(r))
        # True인 index만 추가했기 때문에 0번부터 2번까지 뽑아서 사용
    return a_list[0]*10000+a_list[1]*100+a_list[2]