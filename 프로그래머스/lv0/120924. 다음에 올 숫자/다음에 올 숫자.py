def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        for num in common:
            return common[-1] + common[1] - common[0]
    else:
        return common[-1]*(common[1]//common[0])