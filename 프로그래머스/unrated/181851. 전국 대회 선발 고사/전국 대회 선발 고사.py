def solution(rank, attendance):
    a_list = [rank.index(r) for r in sorted(rank) if attendance[rank.index(r)] == True]
    return a_list[0]*10000+a_list[1]*100+a_list[2]