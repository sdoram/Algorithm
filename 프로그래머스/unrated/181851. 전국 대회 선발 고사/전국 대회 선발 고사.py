def solution(rank, attendance):
    a_list = []
    for r in sorted(rank):
        if attendance[rank.index(r)]:
            a_list.append(rank.index(r))
    return a_list[0]*10000+a_list[1]*100+a_list[2]